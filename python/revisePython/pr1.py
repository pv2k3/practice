class Item:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty
    def calculate_total_price(self, x, y):
        return x*y

item1 = Item("Phone", 500, 5)

item2 = Item("Laptop", 1000, 10)

print(f"{item1.name}   {item1.price}   {item1.qty}")
print(f"{item2.name}   {item2.price}   {item2.qty}")




