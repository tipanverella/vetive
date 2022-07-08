"""
    testing DatePair class
"""
import unittest
from datetime import date
from pydantic import ValidationError
from vetive.date_pair import DatePair


class TestDatePair(unittest.TestCase):
    """unittest for the DatePair class"""

    def setUp(self) -> None:
        self.today = date.today()
        self.no_date = DatePair()
        self.jodia = DatePair()
        self.start = DatePair(start_date="1979-01-12")
        self.end = DatePair(end_date="1979-01-12")
        self.sam = DatePair(end_date="1977-02-13")
        self.odp = DatePair(start_date="1804-01-01", end_date="1979-01-12")

    def test_no_date(self) -> None:
        self.assertTupleEqual(self.no_date.pair, (self.today, self.today))

    def test_start(self) -> None:
        self.assertTupleEqual(self.start.pair, (date(1979, 1, 12), self.today))

    def test_end(self) -> None:
        self.assertTupleEqual(self.end.pair, (date(1979, 1, 12), date(1979, 1, 12)))

    def test_pair(self) -> None:
        self.assertTupleEqual(self.odp.pair, (date(1804, 1, 1), date(1979, 1, 12)))

    def test_unordered_dates(self) -> None:
        with self.assertRaises(ValueError):
            DatePair(start_date="1979-01-31", end_date="1979-01-12")

    def test_bad_start(self) -> None:
        with self.assertRaises(ValidationError):
            DatePair(start_date="1979-01-47")

    def test_bad_end(self) -> None:
        with self.assertRaises(ValidationError):
            DatePair(end_date="1979-01-47")

    def test_bad_both(self) -> None:
        with self.assertRaises(ValidationError):
            DatePair(start_date="1979-01-41", end_date="1979-01-42")

    def test_days(self) -> None:
        self.assertEqual(self.no_date.days, 1)
        self.assertEqual(self.odp.days, 63930)

    def test_contains(self) -> None:
        self.assertTrue(self.odp.contains(self.sam))
        self.assertFalse(self.odp.contains(self.no_date))
        self.assertTrue(self.odp.contains(self.end))
        self.assertFalse(self.odp.contains(self.start))

    def test_overlaps(self) -> None:
        self.assertTrue(self.odp.overlaps(self.sam))
        self.assertFalse(self.odp.overlaps(self.no_date))
        self.assertTrue(self.odp.overlaps(self.end))
        self.assertTrue(self.odp.overlaps(self.start))

    def test_slack_bumper(self) -> None:
        slack = 10
        self.jodia.slack_bumper(slack)
        self.assertEqual(self.jodia.end_date, self.no_date.end_date)
        self.assertEqual(self.jodia.days, self.no_date.days + slack)
        with self.assertRaises(ValueError):
            self.jodia.slack_bumper(0.5)
        with self.assertRaises(ValueError):
            self.jodia.slack_bumper(-1)

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
