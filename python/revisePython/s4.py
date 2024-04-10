import csv


class Item:
    pay_rate = 0.8  # pay rate after the discount of 20%

    all = []

    def __init__(self, name: str, price: float, qty: int):
        # Run validation
        assert price >= 0, f"Price {price} is not greater than zero"
        assert qty >= 0, f"Qty {qty} is not greater than zero"
        self.name = name
        self.price = price
        self.qty = qty

        Item.all.append(self)

    def calculate_total_price(self) -> float:
        return self.price * self.qty

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                qty=int(item.get('qty'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.qty})"

Item.instantiate_from_csv()
print(Item.all)

