"""Generate changed upcoming event images and safely commit them to main."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

BASELINE = Path(".github/event-images-baseline")
EVENTS_FILE = Path("_data/events.yml")
IMAGE_DIR = Path("images/events")
IMAGE_NAME = re.compile(r"images/events/\d+(?:-teaser)?\.jpg\Z")
MAX_ATTEMPTS = 3


class UpdateError(RuntimeError):
    """Raised when a safe image update cannot be completed."""


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )
    if check and result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise UpdateError(f"git {' '.join(args)} failed: {detail}")
    return result


def _blob(repo: Path, object_id: str) -> bytes:
    if not re.fullmatch(r"[0-9a-f]{40,64}", object_id):
        raise UpdateError(f"Invalid event-image baseline object ID: {object_id!r}")
    if git(repo, "cat-file", "-e", f"{object_id}^{{blob}}", check=False).returncode:
        raise UpdateError(
            f"Event-image baseline {object_id} is missing from this checkout. "
            "Restore a valid baseline before retrying."
        )
    return subprocess.run(
        ["git", "cat-file", "blob", object_id],
        cwd=repo,
        check=True,
        capture_output=True,
    ).stdout


def _changed_images(repo: Path) -> list[str]:
    tracked = git(repo, "diff", "--name-only", "--", str(IMAGE_DIR)).stdout.splitlines()
    untracked = git(
        repo,
        "ls-files",
        "--others",
        "--exclude-standard",
        "--",
        str(IMAGE_DIR),
    ).stdout.splitlines()
    paths = sorted(set(tracked + untracked))
    invalid = [path for path in paths if not IMAGE_NAME.fullmatch(path)]
    if invalid:
        raise UpdateError(
            "The image generator changed unexpected files: " + ", ".join(invalid)
        )
    return paths


def _run_generator(
    repo: Path,
    generator: Path,
    generator_root: Path,
    baseline_data: bytes,
    today: date,
) -> None:
    with tempfile.TemporaryDirectory(prefix="website-events-") as directory:
        base_file = Path(directory) / "base-events.yml"
        base_file.write_bytes(baseline_data)
        command = [
            str(generator),
            "website-images",
            "--events-file",
            str((repo / EVENTS_FILE).resolve()),
            "--out-dir",
            str((repo / IMAGE_DIR).resolve()),
            "--base-events-file",
            str(base_file),
            "--site-root",
            str(repo.resolve()),
            "--today",
            today.isoformat(),
        ]
        subprocess.run(command, cwd=generator_root, check=True)


def _set_baseline(repo: Path, object_id: str) -> None:
    destination = repo / BASELINE
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="ascii", dir=destination.parent, delete=False
    ) as temporary:
        temporary.write(object_id + "\n")
        temp_path = Path(temporary.name)
    os.replace(temp_path, destination)


def _is_ancestor(repo: Path, ancestor: str, descendant: str) -> bool:
    return (
        git(repo, "merge-base", "--is-ancestor", ancestor, descendant, check=False).returncode
        == 0
    )


def update_images(
    repo: Path,
    generator: Path,
    generator_root: Path,
    *,
    remote: str = "origin",
    branch: str = "main",
    today: date | None = None,
    max_attempts: int = MAX_ATTEMPTS,
) -> str:
    """Synchronize from the current remote tip, retrying concurrent fast-forwards."""
    repo = repo.resolve()
    generator = generator.resolve()
    generator_root = generator_root.resolve()
    if not (repo / ".git").exists():
        raise UpdateError(f"Not a Git checkout: {repo}")
    if not generator.is_file() or not generator_root.is_dir():
        raise UpdateError("The pinned image-generator executable or checkout is missing.")
    if git(repo, "status", "--porcelain", "--untracked-files=all").stdout.strip():
        raise UpdateError("The website checkout is not clean; refusing to discard local changes.")

    cutoff = today or datetime.now(ZoneInfo("Europe/Vienna")).date()
    initial_head = git(repo, "rev-parse", "HEAD").stdout.strip()
    previous_attempt_images: list[str] = []
    for attempt in range(1, max_attempts + 1):
        git(repo, "fetch", "--no-tags", remote, f"refs/heads/{branch}")
        remote_sha = git(repo, "rev-parse", "FETCH_HEAD").stdout.strip()
        if attempt == 1 and not _is_ancestor(repo, initial_head, remote_sha):
            raise UpdateError(
                f"The checkout {initial_head} is not an ancestor of {remote}/{branch} "
                f"({remote_sha}); refusing to discard divergent commits."
            )
        git(repo, "reset", "--hard", remote_sha)
        for image in previous_attempt_images:
            if git(repo, "ls-files", "--error-unmatch", "--", image, check=False).returncode:
                (repo / image).unlink(missing_ok=True)
        previous_attempt_images = []

        baseline_path = repo / BASELINE
        if not baseline_path.is_file():
            raise UpdateError(f"Missing {BASELINE}; restore a valid processed-event baseline.")
        baseline_id = baseline_path.read_text(encoding="ascii").strip()
        baseline_data = _blob(repo, baseline_id)
        current_id = git(repo, "rev-parse", f"HEAD:{EVENTS_FILE.as_posix()}").stdout.strip()
        if current_id == baseline_id:
            print(f"Event data is already processed at {current_id}; no commit needed.")
            return remote_sha

        _run_generator(repo, generator, generator_root, baseline_data, cutoff)
        previous_attempt_images = _changed_images(repo)
        _set_baseline(repo, current_id)
        git(repo, "add", "--", str(BASELINE), *previous_attempt_images)

        if git(repo, "diff", "--cached", "--quiet", check=False).returncode == 0:
            print("Generated no image or baseline changes; no commit needed.")
            return remote_sha

        env = os.environ.copy()
        env.update(
            {
                "GIT_AUTHOR_NAME": "github-actions[bot]",
                "GIT_AUTHOR_EMAIL": "41898282+github-actions[bot]@users.noreply.github.com",
                "GIT_COMMITTER_NAME": "github-actions[bot]",
                "GIT_COMMITTER_EMAIL": "41898282+github-actions[bot]@users.noreply.github.com",
            }
        )
        subprocess.run(
            ["git", "commit", "-m", "Regenerate event images"],
            cwd=repo,
            env=env,
            check=True,
        )
        commit_sha = git(repo, "rev-parse", "HEAD").stdout.strip()
        push = git(
            repo,
            "push",
            remote,
            f"HEAD:refs/heads/{branch}",
            check=False,
        )

        git(repo, "fetch", "--no-tags", remote, f"refs/heads/{branch}")
        latest_sha = git(repo, "rev-parse", "FETCH_HEAD").stdout.strip()
        if push.returncode == 0 and latest_sha == commit_sha:
            print(f"Committed generated event images and baseline as {commit_sha}.")
            return commit_sha

        if latest_sha != remote_sha and _is_ancestor(repo, remote_sha, latest_sha):
            if attempt < max_attempts:
                print(
                    f"main advanced during image generation; recomputing from {latest_sha} "
                    f"(attempt {attempt + 1}/{max_attempts})."
                )
                continue
            raise UpdateError(
                f"main continued advancing during all {max_attempts} attempts; "
                "no stale generation was accepted. Rerun the workflow on main."
            )

        detail = push.stderr.strip() or push.stdout.strip()
        raise UpdateError(
            f"Could not safely push generated event images to {branch}: "
            f"{detail or 'the remote branch changed non-fast-forward'}"
        )

    raise UpdateError("Image generation exhausted its retry limit.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generator", type=Path, required=True)
    parser.add_argument("--generator-root", type=Path, required=True)
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--branch", default="main")
    parser.add_argument("--today", type=date.fromisoformat)
    args = parser.parse_args()
    try:
        update_images(
            Path.cwd(),
            args.generator,
            args.generator_root,
            remote=args.remote,
            branch=args.branch,
            today=args.today,
        )
    except (OSError, subprocess.CalledProcessError, UpdateError, ValueError) as error:
        print(f"Event image update failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
