import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
UPDATE_SCRIPT = ROOT / "scripts" / "update_event_images.py"
TODAY = "2026-11-05"


FAKE_GENERATOR = """#!/usr/bin/env python3
import argparse
import json
import os
from datetime import date
from pathlib import Path

import yaml

parser = argparse.ArgumentParser()
parser.add_argument("command")
parser.add_argument("--events-file", required=True)
parser.add_argument("--base-events-file", required=True)
parser.add_argument("--out-dir", required=True)
parser.add_argument("--site-root", required=True)
parser.add_argument("--today", required=True)
args = parser.parse_args()
if os.environ.get("FAKE_GENERATOR_FAIL"):
    raise SystemExit("fixture generator failure")
current_text = Path(args.events_file).read_text()
base_text = Path(args.base_events_file).read_text()
current = yaml.safe_load(current_text) or []
base = {event["id"]: event for event in (yaml.safe_load(base_text) or [])}
cutoff = date.fromisoformat(args.today)
generated = []
out_dir = Path(args.out_dir)
out_dir.mkdir(parents=True, exist_ok=True)
for event in current:
    event_id = event["id"]
    if event.get("generate_images", True) is False:
        continue
    if event.get("date") and date.fromisoformat(event["date"]) < cutoff:
        continue
    if base.get(event_id) == event:
        continue
    generated.append(event_id)
    for suffix in ("", "-teaser"):
        (out_dir / f"{event_id}{suffix}.jpg").write_bytes(
            f"generated {event_id}{suffix}".encode()
        )
with open(os.environ["FAKE_GENERATOR_LOG"], "a") as log:
    log.write(json.dumps({
        "base": base_text,
        "current": current_text,
        "generated": generated,
        "today": args.today,
    }) + "\\n")
"""


class EventImageWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.repo = self.root / "website"
        self.remote = self.root / "website.git"
        self.generator_root = self.root / "generator"
        self.generator_root.mkdir()
        self.generator = self.root / "bin" / "imagegen"
        self.generator.parent.mkdir()
        self.generator.write_text(
            FAKE_GENERATOR.replace("#!/usr/bin/env python3", f"#!{sys.executable}"),
            encoding="utf-8",
        )
        self.generator.chmod(0o755)
        self.log = self.root / "generator.jsonl"

        self._git("init", "--bare", "--initial-branch=main", str(self.remote), cwd=self.root)
        self.repo.mkdir()
        self._git("init", "--initial-branch=main", cwd=self.repo)
        self._git("config", "user.name", "Test User", cwd=self.repo)
        self._git("config", "user.email", "test@example.com", cwd=self.repo)
        (self.repo / ".github").mkdir()
        (self.repo / "_data").mkdir()
        (self.repo / "images/events").mkdir(parents=True)

    def _git(self, *args, cwd=None, check=True):
        return subprocess.run(
            ["git", *args],
            cwd=cwd or self.repo,
            check=check,
            capture_output=True,
            text=True,
        )

    def _yaml(self, events):
        return yaml.safe_dump(events, sort_keys=False)

    def _seed(self, events, artwork=()):
        data_path = self.repo / "_data/events.yml"
        data_path.write_text(self._yaml(events), encoding="utf-8")
        blob = self._git("hash-object", "-w", str(data_path)).stdout.strip()
        (self.repo / ".github/event-images-baseline").write_text(blob + "\n")
        for name, content in artwork:
            (self.repo / "images/events" / name).write_bytes(content)
        self._git("add", ".", cwd=self.repo)
        self._git("commit", "-m", "Seed events", cwd=self.repo)
        self._git("remote", "add", "origin", str(self.remote), cwd=self.repo)
        self._git("push", "-u", "origin", "main", cwd=self.repo)
        return blob

    def _push_events(self, events, message):
        (self.repo / "_data/events.yml").write_text(self._yaml(events), encoding="utf-8")
        self._git("add", "_data/events.yml", cwd=self.repo)
        self._git("commit", "-m", message, cwd=self.repo)
        self._git("push", "origin", "main", cwd=self.repo)

    def _run_update(self, extra_env=None):
        env = os.environ.copy()
        env["FAKE_GENERATOR_LOG"] = str(self.log)
        if extra_env:
            env.update(extra_env)
        return subprocess.run(
            [
                sys.executable,
                str(UPDATE_SCRIPT),
                "--generator",
                str(self.generator),
                "--generator-root",
                str(self.generator_root),
                "--today",
                TODAY,
            ],
            cwd=self.repo,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )

    def _generator_calls(self):
        if not self.log.exists():
            return []
        return [json.loads(line) for line in self.log.read_text().splitlines()]

    def _remote_head(self):
        return self._git("rev-parse", "refs/heads/main", cwd=self.repo).stdout.strip()

    def test_seeded_baseline_is_a_noop(self):
        events = [{"id": 52, "title": "Current", "date": "2026-11-25"}]
        self._seed(events)
        before = self._remote_head()

        result = self._run_update()

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self._remote_head(), before)
        self.assertEqual(self._generator_calls(), [])

    def test_multiple_skipped_pushes_generate_only_changed_upcoming_events(self):
        original = [
            {"id": 52, "title": "Old", "date": "2026-11-25"},
            {"id": 53, "title": "Unchanged", "date": "2026-11-26"},
            {"id": 54, "title": "Past old", "date": "2026-10-01"},
            {"id": 55, "title": "Opted in old", "date": "2026-11-27"},
        ]
        artwork = [
            ("53.jpg", b"unchanged custom"),
            ("54.jpg", b"past custom"),
            ("55.jpg", b"opted-out custom"),
            ("55-teaser.jpg", b"opted-out teaser"),
        ]
        original_blob = self._seed(original, artwork)
        first_push = [
            {"id": 52, "title": "First edit", "date": "2026-11-25"}
            if event["id"] == 52
            else event
            for event in original
        ]
        self._push_events(first_push, "First event edit")
        current = [
            {"id": 52, "title": "Latest edit", "date": "2026-11-25"},
            {"id": 53, "title": "Unchanged", "date": "2026-11-26"},
            {"id": 54, "title": "Past changed", "date": "2026-10-01"},
            {
                "id": 55,
                "title": "Opted out changed",
                "date": "2026-11-27",
                "generate_images": False,
            },
            {"id": 56, "title": "New", "date": "2026-12-01"},
        ]
        self._push_events(current, "Second event edit")

        result = self._run_update()

        self.assertEqual(result.returncode, 0, result.stderr)
        calls = self._generator_calls()
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0]["base"], self._yaml(original))
        self.assertEqual(calls[0]["current"], self._yaml(current))
        self.assertEqual(calls[0]["generated"], [52, 56])
        self.assertEqual(calls[0]["today"], TODAY)
        self.assertEqual(
            sorted(path.name for path in (self.repo / "images/events").glob("*.jpg")),
            [
                "52-teaser.jpg",
                "52.jpg",
                "53.jpg",
                "54.jpg",
                "55-teaser.jpg",
                "55.jpg",
                "56-teaser.jpg",
                "56.jpg",
            ],
        )
        self.assertEqual((self.repo / "images/events/53.jpg").read_bytes(), b"unchanged custom")
        self.assertEqual((self.repo / "images/events/54.jpg").read_bytes(), b"past custom")
        self.assertEqual((self.repo / "images/events/55.jpg").read_bytes(), b"opted-out custom")
        self.assertEqual(
            set(self._git("show", "--format=", "--name-only", "HEAD").stdout.splitlines()),
            {
                ".github/event-images-baseline",
                "images/events/52-teaser.jpg",
                "images/events/52.jpg",
                "images/events/56-teaser.jpg",
                "images/events/56.jpg",
            },
        )
        self.assertEqual((self.repo / ".github/event-images-baseline").read_text().strip(),
                         self._git("rev-parse", "HEAD:_data/events.yml").stdout.strip())

        committed = self._remote_head()
        result = self._run_update()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self._remote_head(), committed)
        self.assertEqual(len(self._generator_calls()), 1)
        self.assertEqual(
            self._git("cat-file", "blob", original_blob).stdout,
            calls[0]["base"],
        )

    def test_generator_failure_does_not_advance_the_baseline(self):
        original = [{"id": 52, "title": "Old", "date": "2026-11-25"}]
        self._seed(original)
        changed = [{"id": 52, "title": "New", "date": "2026-11-25"}]
        self._push_events(changed, "Change event")
        baseline_path = self.repo / ".github/event-images-baseline"
        before = baseline_path.read_text()

        result = self._run_update({"FAKE_GENERATOR_FAIL": "1"})

        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(baseline_path.read_text(), before)

    def test_invalid_baseline_fails_without_running_generator(self):
        events = [{"id": 52, "title": "Current", "date": "2026-11-25"}]
        self._seed(events)
        baseline_path = self.repo / ".github/event-images-baseline"
        baseline_path.write_text("not-a-git-blob\n", encoding="ascii")
        self._git("add", str(baseline_path), cwd=self.repo)
        self._git("commit", "-m", "Corrupt event baseline", cwd=self.repo)
        self._git("push", "origin", "main", cwd=self.repo)

        result = self._run_update()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Invalid event-image baseline", result.stderr)
        self.assertEqual(self._generator_calls(), [])

    def test_missing_baseline_fails_clearly(self):
        events = [{"id": 52, "title": "Current", "date": "2026-11-25"}]
        self._seed(events)
        self._git("rm", ".github/event-images-baseline", cwd=self.repo)
        self._git("commit", "-m", "Remove event baseline", cwd=self.repo)
        self._git("push", "origin", "main", cwd=self.repo)

        result = self._run_update()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Missing .github/event-images-baseline", result.stderr)
        self.assertEqual(self._generator_calls(), [])

    def test_non_fast_forward_race_recomputes_without_losing_newer_commit(self):
        original = [{"id": 52, "title": "Old", "date": "2026-11-25"}]
        self._seed(original)
        changed = [{"id": 52, "title": "New", "date": "2026-11-25"}]
        self._push_events(changed, "Change event")
        competitor = self.root / "competitor"
        self._git("clone", str(self.remote), str(competitor), cwd=self.root)
        self._git("config", "user.name", "Concurrent User", cwd=competitor)
        self._git("config", "user.email", "concurrent@example.com", cwd=competitor)

        wrapper_dir = self.root / "git-wrapper"
        wrapper_dir.mkdir()
        wrapper = wrapper_dir / "git"
        real_git = shutil.which("git")
        wrapper.write_text(
            f"""#!{sys.executable}
import os
import subprocess
import sys
from pathlib import Path

real_git = os.environ["REAL_GIT"]
if sys.argv[1:2] == ["push"] and not Path(os.environ["RACE_MARKER"]).exists():
    Path(os.environ["RACE_MARKER"]).touch()
    repo = os.environ["COMPETITOR_REPO"]
    subprocess.run([real_git, "-C", repo, "pull", "--ff-only", "origin", "main"], check=True)
    Path(repo, "concurrent-change.txt").write_text("kept\\n")
    subprocess.run([real_git, "-C", repo, "add", "concurrent-change.txt"], check=True)
    subprocess.run([real_git, "-C", repo, "commit", "-m", "Concurrent website update"], check=True)
    subprocess.run([real_git, "-C", repo, "push", "origin", "main"], check=True)
os.execv(real_git, [real_git, *sys.argv[1:]])
""",
            encoding="utf-8",
        )
        wrapper.chmod(0o755)
        env = {
            "PATH": str(wrapper_dir) + os.pathsep + os.environ["PATH"],
            "REAL_GIT": real_git,
            "COMPETITOR_REPO": str(competitor),
            "RACE_MARKER": str(self.root / "race-started"),
        }

        result = self._run_update(env)

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("recomputing from", result.stdout)
        self.assertEqual(len(self._generator_calls()), 2)
        self.assertEqual(
            self._git(
                "--git-dir",
                str(self.remote),
                "show",
                "refs/heads/main:concurrent-change.txt",
                cwd=self.root,
            ).stdout.strip(),
            "kept",
        )
        self.assertEqual(
            self._git(
                "--git-dir",
                str(self.remote),
                "show",
                "refs/heads/main:images/events/52.jpg",
                cwd=self.root,
            ).stdout.strip(),
            "generated 52",
        )

    def test_event_artwork_precedence_and_fallbacks(self):
        layout = (ROOT / "_layouts/event.html").read_text(encoding="utf-8")
        upcoming = (ROOT / "_includes/upcoming-events.html").read_text(encoding="utf-8")
        event_image_check = layout.index("{% if event_image_file %}")
        teaser_check = layout.index("{% elsif teaser_file %}", event_image_check)
        self.assertLess(event_image_check, teaser_check)
        self.assertIn("assign artwork_path = event_image_path", layout)
        self.assertIn("assign artwork_path = teaser_path", layout)
        self.assertIn("placeholder-website.png", layout)
        self.assertIn("assign event_image_path = teaser_path", upcoming)
        self.assertIn("placeholder-teaser.png", upcoming)


if __name__ == "__main__":
    unittest.main()
