#  https://lms.10x.org.il/item/293/

# special_boom_calendar.py
import calendar
import time


# ------- YOUR CODE HERE --------------------
# -------------------------------------------
class BoomTextCalendar(calendar.TextCalendar):

    def formatday(self, day: int, weekday: int, width: int) -> str:
        super_val = super().formatday(day, weekday, width)
        try:
            val = int(super_val.strip())
            if (not val % self.boom_value and val > self.boom_value) or str(
                self.boom_value
            ) in str(val):
                super_val = "**"
        finally:
            return super_val


class SpecialDayCalendar(calendar.TextCalendar):

    def formatday(self, day: int, weekday: int, width: int) -> str:
        super_val = super().formatday(day, weekday, width)
        try:
            val = int(super_val.strip())
            if val in self.special_days:
                super_val = ":)"
        finally:
            return super_val


class SpecialBoom3Mixin:
    boom_value = 3
    special_days = [
        10,
        11,
        12,
        13,
    ]


class Boom7Calendar(BoomTextCalendar):
    boom_value = 7


class Boom6Calendar(BoomTextCalendar):
    boom_value = 6


class HappyDaysCalendar(SpecialDayCalendar):
    special_days = [2, 13, 17, 31]


class SpecialBoom7Calendar(SpecialDayCalendar, BoomTextCalendar):
    boom_value = 7
    special_days = [16, 23, 30]


class SpecialBoom6Calendar(SpecialDayCalendar, BoomTextCalendar):
    boom_value = 6
    special_days = [1, 31]


class SpecialBoom3Calendar(SpecialBoom3Mixin, SpecialDayCalendar, BoomTextCalendar):
    pass


class Boom3SpecialCalendar(SpecialBoom3Mixin, BoomTextCalendar, SpecialDayCalendar):
    pass


TESTS = {
    Boom7Calendar: """
     July 2019
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6 **
 8  9 10 11 12 13 **
15 16 ** 18 19 20 **
22 23 24 25 26 ** **
29 30 31
""",
    Boom6Calendar: """
     July 2019
Mo Tu We Th Fr Sa Su
 1  2  3  4  5 **  7
 8  9 10 11 ** 13 14
15 ** 17 ** 19 20 21
22 23 ** 25 ** 27 28
29 ** 31
""",
    HappyDaysCalendar: """
     July 2019
Mo Tu We Th Fr Sa Su
 1 :)  3  4  5  6  7
 8  9 10 11 12 :) 14
15 16 :) 18 19 20 21
22 23 24 25 26 27 28
29 30 :)
""",
    SpecialBoom7Calendar: """
     July 2019
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6 **
 8  9 10 11 12 13 **
15 :) ** 18 19 20 **
22 :) 24 25 26 ** **
29 :) 31
""",
    SpecialBoom6Calendar: """
     July 2019
Mo Tu We Th Fr Sa Su
:)  2  3  4  5 **  7
 8  9 10 11 ** 13 14
15 ** 17 ** 19 20 21
22 23 ** 25 ** 27 28
29 ** :)
""",
    SpecialBoom3Calendar: """
     July 2019
Mo Tu We Th Fr Sa Su
 1  2 **  4  5 **  7
 8 ** :) :) :) :) 14
** 16 17 ** 19 20 **
22 ** ** 25 26 ** 28
29 ** **
""",
    Boom3SpecialCalendar: """
     July 2019
Mo Tu We Th Fr Sa Su
 1  2 **  4  5 **  7
 8 ** :) :) ** ** 14
** 16 17 ** 19 20 **
22 ** ** 25 26 ** 28
29 ** **
""",
}

for cls, expected in TESTS.items():
    expected = expected.lstrip("\n")
    print(f"==== Expected {cls.__name__} ====")
    print(expected)
    print(f"==== Result {cls.__name__} ====")
    o = cls()
    result = o.formatmonth(2019, 7)
    print(result)
    time.sleep(0.1)  # for pycharm stderr bug :-(
    assert result == expected
    print("OK")
    print()

print("DONE :-)")
