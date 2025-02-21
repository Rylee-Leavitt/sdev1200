#
# Rylee Leavitt
# 2/17/25
# Cash Register Programming Project
# SDEV 1200
#

class RetailItem:
    def __init__(self, description, units, price):
        self.description = description
        self.units = units
        self.price = price

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

# Demonstration program
def main():
    # Create some RetailItem objects
    item1 = RetailItem("Astarion Plush", 1, 29.99)
    item2 = RetailItem("Baulders Gate candle", 3, 49.99)
    item3 = RetailItem("Pale Elf cards", 10, 19.99)

    # Create a CashRegister object
    register = CashRegister()

    # Add items to the cash register
    register.purchase_item(item1)
    register.purchase_item(item2)
    register.purchase_item(item3)

    # Display the items and the total
    print("Items purchased:")
    register.show_items()
    print(f"\nTotal price: ${register.get_total():.2f}")

    # Clear the cash register
    register.clear()

# Run the demonstration
if __name__ == "__main__":
    main()