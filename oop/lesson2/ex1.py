# https://lms.10x.org.il/item/116/
import calendar


class MyTextCalendar(calendar.TextCalendar):

    def formatday(self, day: int, weekday: int, width: int) -> str:
        super_val = super().formatday(day, weekday, width)
        try:
            val = int(super_val.strip())
            if (not val % 7 and val > 6) or "7" in str(val):
                super_val = "**"
        finally:
            return super_val

    pass


c = MyTextCalendar()
result = c.formatmonth(2014, 5)

expected = """      May 2014
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6 **  8  9 10 11
12 13 ** 15 16 ** 18
19 20 ** 22 23 24 25
26 ** ** 29 30 31
"""
print("Expected:")
print("-" * 40)
print(expected)
print("-" * 40)
print("My calendar:")
print("-" * 40)
print(result)
print("-" * 40)

assert result == expected

print("OK")
