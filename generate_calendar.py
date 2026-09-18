import hashlib
from datetime import datetime

import pytz
import yaml
from icalendar import Calendar, Event

# ---- SETTINGS ----
TIMEZONE = "Europe/Berlin"  # Change to your time zone, e.g. "America/New_York"
CALENDAR_NAME = "Cloud Native Linz Events"
CALENDAR_DESCRIPTION = "Meetup events for the Cloud Native Linz community"
SITE_URL = "https://cloudnativelinz.at"

def generate_calendar(events):
    calendar = Calendar()
    calendar.add("prodid", "-//Cloud Native Linz Calendar//EN")
    calendar.add("version", "2.0")
    calendar.add("x-wr-calname", CALENDAR_NAME)
    calendar.add("x-wr-caldesc", CALENDAR_DESCRIPTION)
    calendar.add("name", CALENDAR_NAME)

    timezone = pytz.timezone(TIMEZONE)

    for event_data in events:
        event = Event()
        event_url = f"{SITE_URL}/events/meetup/{event_data['slug']}/"
        event_date = datetime.strptime(event_data["date"], "%Y-%m-%d")

        if event_data.get("doors_open"):
            start_hour, start_minute = map(int, event_data["doors_open"].split(":"))
        else:
            start_hour = 18
            start_minute = 0

        start_dt = timezone.localize(
            event_date.replace(hour=start_hour, minute=start_minute)
        )
        end_dt = timezone.localize(
            event_date.replace(hour=start_hour + 3, minute=start_minute)
        )

        event.add("summary", f"{event_data['title']} - CNCF Linz")
        event.add("dtstart", start_dt)
        event.add("dtend", end_dt)

        location = event_data.get("address") or event_data.get("host", "TBA")
        if location and location.lower() != "online":
            event.add("location", location)
        elif location and location.lower() == "online":
            event.add("location", "Online Event")

        description = f"Host: {event_data.get('host', 'TBA')}\n"
        if event_data.get("talks"):
            description += "Talks:\n"
            for talk in event_data["talks"]:
                description += f"- {talk['title']} by {talk['speaker']}\n"
        description += f"\nAll information: {event_url}"
        if "event_link" in event_data:
            description += f"\n\nRSVP: {event_data['event_link']}"

        event.add("description", description)

        uid_hash = hashlib.sha256(str(event_data["id"]).encode()).hexdigest()
        event.add("uid", f"{uid_hash}@cncflinz.at")
        calendar.add_component(event)

    return calendar


def main():
    with open("_data/events.yml") as events_file:
        events = yaml.safe_load(events_file)

    with open("calendar.ics", "wb") as calendar_file:
        calendar_file.write(generate_calendar(events).to_ical())


if __name__ == "__main__":
    main()
