class MyClass:
    print("b")
    x = 1
    items = []

    def __init__(self) -> None:
        print("c")
        self.x = 2
        self.items = []


print(MyClass.x)
print(MyClass.items)

o = MyClass()
print(o.x)
print(o.items)
