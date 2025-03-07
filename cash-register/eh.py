class CashRegister:
    def __init__(self):
        self.items = []

    def purchase_item(self, item):
        self.items.append(item)

    def get_total(self):
        total = sum(item.price for item in self.items)
        return total

    def show_items(self):
        for item in self.items:
            print(f"Description: {item.description}, Units: {item.units}, Price: ${item.price:.2f}")

    def clear(self):
        self.items = []
