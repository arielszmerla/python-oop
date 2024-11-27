# pydantic_departments.py

from __future__ import annotations

import datetime
import json
from enum import Enum
from pprint import pp

import pydantic


class EmployeeLevel(str, Enum):
    DIRECTOR = "Director"
    MANAGEMENT = "Management"
    SENIOR = "Senior"
    JUNIOR = "Junior"

    def __repr__(self):
        return str(self)

class Address(pydantic.BaseModel):
    street: str
    city: str
    country: str
    zip: str

class Employee(pydantic.BaseModel):
    employee_id: int
    name: str
    salary: float
    level: EmployeeLevel
    phone: str
    birthday: datetime.date
    address: Address


class Departement(pydantic.BaseModel):

      title: str
      employees: list[Employee] = []
  
class Company(pydantic.BaseModel):
    company_name: str
    departments: list[Departement] = []
    def number_of_employees(self):
        return [e  for d in self.departments for e in d.employees].__len__()
    def total_salaries(self):
        return sum([e.salary  for d in self.departments for e in d.employees])
    def get_employees_by_level(self, level):
         return [tuple([e.name, e.salary])  for d in self.departments for e in d.employees if e.level ==level]



# ---- YOUR CODE HERE -----------------
# DEFINE YOUR PYDANTIC MODELS HERE
# -------------------------------------

with open(r"C:\Users\arielsz\Downloads\company2b.json") as f:
    company = Company(**json.load(f))

num = company.number_of_employees()
print("Total employees:", num)
assert num == 66
print("OK1")

salary = company.total_salaries()
print("Total salary:", salary)
assert salary == 1338800
print("OK2")

result = company.get_employees_by_level(EmployeeLevel.DIRECTOR)
pp(result)
assert isinstance(result, list), type(result)
assert len(result) == 3, len(result)
t0 = result[0]
assert isinstance(t0, tuple), type(t0)
assert len(t0) == 2, len(t0)
name, e = t0
assert name == "Hardware Engineering", repr(name)
assert isinstance(e, Employee), type(e)
assert e.name == "Charles Green", e
print("OK3A")
assert isinstance(e.level, EmployeeLevel)
assert e.birthday == datetime.date(1974, 2, 21), e
print("OK3B")

print("Good!!!!")