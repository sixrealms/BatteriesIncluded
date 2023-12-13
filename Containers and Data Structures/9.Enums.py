'''f you accidentally pass an invalid value to schedule_task, such as an integer or a string, you'll get a clear error.
Enumerations help to enforce type safety and provide a clear set of allowed values. They make your code more expressive
and self-documenting.'''

from enum import Enum, auto


class DayOfWeek(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()


def schedule_task(day):
    if day == DayOfWeek.MONDAY:
        print("Prepare for week ahead")
    elif day == DayOfWeek.FRIDAY:
        print("Get ready for the weekend")
    else:
        print("Do regular tasks")


schedule_task(DayOfWeek.SUNDAY)
schedule_task(DayOfWeek.MONDAY)
