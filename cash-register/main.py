#
# Rylee Leavitt
# 2/17/25
# Cash Register Programming Project
# SDEV 1200
#

class RetailItem:
    #RetailItem Class: This class represents items that can be sold (3)

    def __init__(self, description, units, price):
        #Initializes the RetailItem class with an empty list of items.

        self.description = description #Description of the items
        self.units = units             #units of the items
        self.price = price             #price of the items

class CashRegister: 
    #CashRegister Class stores store RetailItem objects

    def __init__(self):
        #Initializes the CashRegister object with an empty list of items.

        self.items = []

    def purchase_item(self, item):
        #purchase_item: Adds a RetailItem object to the items list.

        self.items.append(item)

    def get_total(self):
        #get_total: Calculates and returns the total price of all the items in the items list.

        total = sum(item.price for item in self.items) 
        #Calculates the total price of all the items in the items list.

        return total 
        #returns the total price of all the items in the items list.

    def show_items(self):
        #Displays the description, units, and price of each item

        for item in self.items:
            print(f"Description: {item.description}, Units: {item.units}, Price: ${item.price:.2f}")
            # Returns Ex) "Description: Astarion Plush, Units: 1, Price: $29.99"

    def clear(self):
        self.items = []

# Demonstration program
def main():
    # Create some RetailItem objects
    #name, units, price

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