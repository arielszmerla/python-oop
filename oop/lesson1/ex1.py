# context manager implementation https://lms.10x.org.il/item/131/

import time


class MyProfiler:
    def __init__(self, name):
        self.start = time.perf_counter()
        self.name = name
        pass

    
    def __enter__(self):
        
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"@@@ {self.name} took {c.elapsed():.1f}s. no error")

    
    def elapsed(self):
        return (time.perf_counter() - self.start)




print("--- Part 1 ---")
print("> Before Block")
with MyProfiler("foo") as c:
    time.sleep(0.5)
    print("> In Block")
print("> After Block")

print()

print("--- Part 2 ---")
with MyProfiler("bar") as c:
    time.sleep(0.5)
    print(f"Elapsed: {c.elapsed():.1f}s.")
    time.sleep(0.5)

print()

print("--- Part 3 ---")
with MyProfiler("baz") as c:
    time.sleep(0.5)
    1 / 0