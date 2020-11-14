import datetime
from typing import List


class DaysOfWeekChecker:
    """
    Checks if the current day of the week is present in the list of days of week.
    """

    def __init__(self, days_of_week: List[int], *args, **kwargs) -> None:
        self.days_of_week = days_of_week

    def _current_day_of_week(self) -> int:
        return datetime.datetime.today().weekday()

    def check(self) -> bool:
        return self._current_day_of_week() in self.days_of_week
