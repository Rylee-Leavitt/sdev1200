#
# Rylee Leavitt
# 2/17/25
# Cash Register Programming Project
# SDEV 1200
#

#cash_Register.py

#From retail.py
from retail import RetailItem

# CashRegister.py
# Defines the CashRegister class

class CashRegister:
    # Defines a class named CashRegister to manage purchased items

    def __init__(self):
        # Initializes an empty list to hold RetailItem objects
        self.items = []

    def purchase_item(self, retail_item):
        # Adds a RetailItem object to the list of purchased items
        self.items.append(retail_item)

    def get_total(self):
        # Calculates the total price of all purchased items
        return sum(item.price for item in self.items)

    def show_items(self):
        # Displays all the items in the cash register
        if not self.items:
            print("No items have been added to the cart.")
        else:
            for item in self.items:
                print(item)

    def clear(self):
        # Clears the list of purchased items
        self.items = []