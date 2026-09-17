import hashlib
import unittest
from datetime import timedelta

from generate_calendar import CALENDAR_NAME, generate_calendar


class GenerateCalendarTests(unittest.TestCase):
    def setUp(self):
        self.event_data = {
            "id": 42,
            "title": "Cloud Native Test Meetup",
            "slug": "cloud-native-test-meetup",
            "date": "2026-09-29",
            "doors_open": "17:30",
            "host": "Test Host",
            "address": "Test Street 1, Linz",
            "event_link": "https://example.com/rsvp",
            "talks": [{"title": "A Test Talk", "speaker": "Ada Example"}],
        }

    def generate_event(self, event_data=None):
        calendar = generate_calendar([event_data or self.event_data])
        return calendar.walk("VEVENT")[0]

    def test_calendar_and_event_metadata(self):
        calendar = generate_calendar([self.event_data])
        event = calendar.walk("VEVENT")[0]

        self.assertEqual(str(calendar["x-wr-calname"]), CALENDAR_NAME)
        self.assertEqual(str(event["summary"]), "Cloud Native Test Meetup - CNCF Linz")
        self.assertEqual(str(event["location"]), "Test Street 1, Linz")
        expected_uid = hashlib.sha256(b"42").hexdigest() + "@cncflinz.at"
        self.assertEqual(str(event["uid"]), expected_uid)

    def test_event_page_and_rsvp_links_are_included(self):
        event = self.generate_event()
        event_url = (
            "https://cloudnativelinz.at/events/meetup/cloud-native-test-meetup/"
        )

        self.assertEqual(str(event["url"]), event_url)
        self.assertIn(f"Event details: {event_url}", str(event["description"]))
        self.assertIn("RSVP: https://example.com/rsvp", str(event["description"]))

    def test_time_uses_doors_open_and_has_three_hour_duration(self):
        event = self.generate_event()
        start = event.decoded("dtstart")
        end = event.decoded("dtend")

        self.assertEqual((start.hour, start.minute), (17, 30))
        self.assertEqual(start.tzinfo.zone, "Europe/Berlin")
        self.assertEqual(end - start, timedelta(hours=3))

    def test_defaults_to_six_pm_and_online_location(self):
        event_data = self.event_data | {"host": "online"}
        event_data.pop("address")
        event_data.pop("doors_open")
        event_data.pop("event_link")

        event = self.generate_event(event_data)

        self.assertEqual((event.decoded("dtstart").hour, event.decoded("dtstart").minute), (18, 0))
        self.assertEqual(str(event["location"]), "Online Event")
        self.assertNotIn("RSVP:", str(event["description"]))

    def test_talks_are_listed_in_description(self):
        description = str(self.generate_event()["description"])

        self.assertIn("Talks:\n- A Test Talk by Ada Example", description)


if __name__ == "__main__":
    unittest.main()