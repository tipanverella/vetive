"""
    This module implements an ordered date pair class,
    suitable for date ranges
"""
from datetime import date, timedelta
from typing import Optional, Tuple
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

    @property
    def pair(self) -> Tuple[date, date]:
        """
        Convenient tuple version of the object
        :return:
        """

    def contains(self, val) -> bool:
        """Checks if the val provided is contained in the current DatePair"""
        res = False
        return res

    def overlaps(self, val) -> bool:
        """Checks if the val provided overlaps with the current DatePair"""
        res = False
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
