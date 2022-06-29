"""
    This module implements an ordered date pair class,
    suitable for date ranges
"""
from datetime import date, datetime, timedelta
from typing import Optional, Tuple
from typing_extensions import Self
from pydantic import BaseModel, root_validator


class DatePair(BaseModel):
    """
    The Ordered Date Pair class
    """

    start_date: Optional[date] = None
    end_date: Optional[date] = None

    @root_validator()
    # pylint: disable=no-self-argument
    def valid_date_pair(cls, values):
        """
        This function makes sure that the dates are proper.
        It is the entire raison-d'etre of this class
        :param values:
        :return:
        """
        # no values provided
        # pylint: disable=no-else-raise
        if not values:
            raise ValueError("an invalid date was provided!")
        elif not any(values.values()):
            values["start_date"] = date.today()
            values["end_date"] = date.today()
        # at least one value provided
        else:
            if not values["end_date"]:
                values["end_date"] = date.today()
            elif not values["start_date"]:
                values["start_date"] = values["end_date"]
        if values["start_date"] > values["end_date"]:
            raise ValueError("start_date is GREATER than end_date!")
        return values

    @property
    def days(self) -> int:
        """
        The number of days in the range
        :return:
        """
        days = self.end_date - self.start_date + timedelta(days=1)
        return days.days

    @property
    def pair(self) -> Tuple[date, date]:
        """
        Convenient tuple version of the object
        :return:
        """
        return self.start_date, self.end_date

    def contains(self, val) -> bool:
        """Checks if the val provided is contained in the current DatePair"""
        res = False
        if isinstance(val, DatePair):
            if self.start_date <= val.start_date and self.end_date >= val.end_date:
                res = True
        elif isinstance(val, date or datetime):
            if self.start_date <= val <= self.end_date:
                res = True
        else:
            raise ValueError(
                "The argument value given must be either a datepair, a date or a datetime object"
            )
        return res

    def overlaps(self, val) -> bool:
        """Checks if the val provided overlaps with the current DatePair"""
        res = False
        if isinstance(val, DatePair):
            if self.start_date < val.start_date and self.end_date < val.end_date:
                res = True
            elif val.start_date < self.start_date and val.end_date < self.end_date:
                res = True
            elif val.start_date == self.start_date and val.end_date > self.end_date:
                res =True
            elif val.start_date < self.start_date and val.end_date == self.end_date:
                res = True
        else:
            raise ValueError(
                "The argument value given must be either a datepair, a date or a datetime object"
            )
        return res

    def slack_bumper(self, val: int):
        """
        pushes the start_date back by val days
        :param val:
        :return:
        """
        if not isinstance(val, int):
            raise ValueError(f"{val} should be an integer!")
        if val < 0:
            raise ValueError(f"{val} should be non negative!")
        self.start_date -= timedelta(days=val)

