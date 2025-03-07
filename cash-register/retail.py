#
# Rylee Leavitt
# 2/9/25
# RetailItem Class Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program. 

class RetailItem: 
    #defines a class named RetailItem

    def __init__(self, description, units, price): #initializes class attributes
        self.description = description  #initializes desc
        self.units = units              #initializes units
        self.price = price              #initializes price

    def __str__(self):
        #defines what goes in the print string /Summary
        return f"Description: {self.description}, Units in Inventory: {self.units}, Price: ${self.price:.2f}"

# Creating three RetailItem objects
item1 = RetailItem("Jacket", 12, 59.95) 
# Describes the jacket item, 12 units, and $59.95

item2 = RetailItem("Designer Jeans", 40, 34.95)
# Describes the Designer Jeans item, 40 units, and $34.95

item3 = RetailItem("Shirt", 20, 24.95)
# Describes the shirt item, 20 units, and $24.95

# Displaying the data of each RetailItem object
print(item1)
print(item2)
print(item3)