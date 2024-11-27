import random

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.color = random.choice(["red", "green", "blue"])

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def size(self):
        return self.x ** 2 + self.y ** 2
    
    def add_points(self, other):
        return Point(self.x + other.x, self.y + other.y)


    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

p1 = Point(5, 7)
p2 = Point(10, 16)
p3 = p1.add_points( p2)

assert p3 == Point(15, 23)
print("ok")
