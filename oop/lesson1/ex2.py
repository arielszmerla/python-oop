from collections import Counter  #### USE ME!!!! https://lms.10x.org.il/item/308/
import sys
import time
import logging


class AutoCounter:
    def __init__(self, name, file="def"):
        self.name = name
        self.file = file

    def __enter__(self):
        self.counter = Counter()
        return self.counter

    def __exit__(self, exc_type, exc_val, exc_tb):
        for k in sorted(self.counter.items()):
            print(f"*  {k[0]}: {k[1]}")
        return self

    pass


print("Starting Part 1...")

with AutoCounter("Results:", file=sys.stdout) as c:
    c["foo"] += 1
    c["foo"] += 1
    c["bar"] += 1
    c["baz"] = 123
    c["z"] += 1
    c["a"] += 1
    c["A"] += 1

time.sleep(0.1)

print("... Part 1 Done. OK")

time.sleep(0.1)

print("Starting Part 2...")

time.sleep(0.1)

with AutoCounter("Results:") as c:
    c["foo"] += 1
    c["bar"] += 1
    c["baz"] = 123
    x = 1 / 0


import random

with AutoCounter("Outer:") as outer:
    for i in range(50):
        with AutoCounter(f"Loop #{i + 1}") as inner:
            for j in range(random.randint(5, 10)):
                inner[random.choice("abcdefghij")] += 1
                if random.randint(1, 40) == 13:
                    raise ValueError("bad luck!")
            outer += inner
            outer["loops completed"] += 1
