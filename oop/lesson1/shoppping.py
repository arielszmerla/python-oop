class ShoppingCart:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def show_items(self):
        print(f"Items in {self.name.title()}'s cart:")
        for item in self.items:
            print("-", item)

cart1 = ShoppingCart("Ariel")
cart1.add_item("apple")
cart1.add_item("banana")
cart1.add_item("cereal")
cart1.show_items()