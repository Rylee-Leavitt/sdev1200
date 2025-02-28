#
# Rylee Leavitt
# 2/17/25
# Cash Register Programming Project
# SDEV 1200
#

#cash_Register.py

#From retail.py
from retail import RetailItem

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
        register.show_items()
        
        for item in self.items:
            print(f"Description: {item.description}, Units: {item.units}, Price: ${item.price:.2f}")
            # Returns Ex) 

    def clear(self):
        self.items = []

        # Clear the cash register