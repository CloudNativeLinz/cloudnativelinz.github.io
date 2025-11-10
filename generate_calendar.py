import yaml
import hashlib
from datetime import datetime
from icalendar import Calendar, Event
import pytz

# ---- SETTINGS ----
TIMEZONE = "Europe/Berlin"  # Change to your time zone, e.g. "America/New_York"
CALENDAR_NAME = "Cloud Native Linz Events"
CALENDAR_DESCRIPTION = "Meetup events for the Cloud Native Linz community"

# Load YAML
with open("_data/events.yml", "r") as f:
    data = yaml.safe_load(f)

# Prepare calendar
cal = Calendar()
cal.add("prodid", "-//Cloud Native Linz Calendar//EN")
cal.add("version", "2.0")
cal.add("x-wr-calname", CALENDAR_NAME)  # Calendar name (widely supported)
cal.add("x-wr-caldesc", CALENDAR_DESCRIPTION)  # Calendar description
cal.add("name", CALENDAR_NAME)  # Standard property for calendar name

tz = pytz.timezone(TIMEZONE)

for ev in data:
    event = Event()

    # Parse date
    event_date = datetime.strptime(ev["date"], "%Y-%m-%d")
    
    # Use doors_open time if available, otherwise default to 18:00 (6pm)
    if 'doors_open' in ev and ev['doors_open']:
        # Parse the doors_open time (format: 'HH:MM')
        time_parts = ev['doors_open'].split(':')
        start_hour = int(time_parts[0])
        start_minute = int(time_parts[1])
    else:
        start_hour = 18
        start_minute = 0
    
    start_dt = tz.localize(event_date.replace(hour=start_hour, minute=start_minute))
    # End time is 3 hours after start
    end_dt = tz.localize(event_date.replace(hour=start_hour + 3, minute=start_minute))

    event.add("summary", ev["title"])
    event.add("dtstart", start_dt)
    event.add("dtend", end_dt)
    
    # Add location information - prefer address field if available, otherwise use host
    location = ev.get('address') if 'address' in ev and ev['address'] else ev.get('host', 'TBA')
    if location and location.lower() != 'online':
        event.add("location", location)
    elif location and location.lower() == 'online':
        event.add("location", "Online Event")

    # Add the event link as URL
    if 'event_link' in ev:
        event.add("url", ev['event_link'])

    # Create description from talks if available
    description = f"Host: {ev.get('host', 'TBA')}\n"
    if 'talks' in ev and ev['talks']:
        description += "Talks:\n"
        for talk in ev['talks']:
            description += f"- {talk['title']} by {talk['speaker']}\n"
    if 'event_link' in ev:
        description += f"\nEvent link (RSVP): {ev['event_link']}"

    event.add("description", description)

    # Create stable UID by hashing title + date
    uid_base = f"{ev['id']}"
    uid_hash = hashlib.md5(uid_base.encode("utf-8")).hexdigest()
    event.add("uid", f"{uid_hash}@cncflinz.at")

    cal.add_component(event)

# Save ICS
with open("calendar.ics", "wb") as f:
    f.write(cal.to_ical())
