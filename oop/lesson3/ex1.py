# company_flat1_pydantic.py
from __future__ import annotations

import datetime
import json
from pprint import pprint

import pydantic


class Employee(pydantic.BaseModel):
    employee_id: int
    name: str
    position: str
    salary: float
    phone: str
    birthday: datetime.date
    address: Address


class Address(pydantic.BaseModel):

    street: str
    city: str
    country: str
    zip: str


# ---- YOUR CODE HERE -----------------
# DEFINE YOUR PYDANTIC MODELS HERE
# -------------------------------------


def total_salaries(employees: list[Employee]):
    return sum(e.salary for e in employees)

    pass
    # -------------------------------------


def total_salaries_for_position(employees: list[Employee], position: str):
    return sum(e.salary for e in employees if e.position == position)
    pass
    # -------------------------------------


def get_birthdays_for_day(employees: list[Employee], month: int, day: int):
    return [e for e in employees if e.birthday.day == day and e.birthday.month == month]
    # ---- YOUR CODE HERE -----------------
    # -------------------------------------


with open(r"C:\Users\arielsz\Downloads\company1.json", encoding="utf8") as f:
    all_employees = [Employee(**d) for d in json.load(f)]

result1 = total_salaries(all_employees)
print("total salary:", result1)
assert result1 == 1979800
print("OK1")
print()

result2 = total_salaries_for_position(all_employees, "Developer")
print("Developer's salary:", result2)
assert result2 == 1073700
print("OK2")
print()

june24 = get_birthdays_for_day(all_employees, 6, 24)
print("Birthdays for June 24th:", june24)
assert june24 == []
print("OK3")
print()

march12 = get_birthdays_for_day(all_employees, 3, 12)
print("Birthdays for March 12th:")
pprint(march12)
assert isinstance(march12, list)
assert len(march12) == 2
assert [e.employee_id for e in march12] == [70140, 99407]
print("OK4")
print()

dec8 = get_birthdays_for_day(all_employees, 12, 8)
print("Birthdays for December 8th:")
pprint(dec8)
assert isinstance(dec8, list)
assert len(dec8) == 1
e = dec8[0]
assert isinstance(e, Employee)
assert e.employee_id == 30792
assert e.name == "Michael Brooks"
assert e.phone == "02-8780-947"
assert e.birthday == datetime.date(1984, 12, 8)
assert isinstance(e.address, Address)
assert e.address.zip == "70333"
assert e.address.dict() == {
    "street": "070 Parker Point",
    "city": "Lisashire",
    "country": "Saint Kitts and Nevis",
    "zip": "70333",
}
print("OK5")
print()

print("Great!!!")
