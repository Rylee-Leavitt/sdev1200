#
# Rylee Leavitt
# 2/17/25
# Cash Register Programming Project
# SDEV 1200
#

#Main py
# main.py
# Demonstrates the usage of the RetailItem and CashRegister classes

from retail import RetailItem
from cash_Register import CashRegister

def main():
    # Create RetailItem objects
    item1 = RetailItem("Jacket", 12, 59.95)
    item2 = RetailItem("Designer Jeans", 40, 34.95)
    item3 = RetailItem("Shirt", 20, 24.95)

    # Create a CashRegister object
    register = CashRegister()

    print("Adding items to the cart...\n")
    # Add items to the cash register
    register.purchase_item(item1)
    register.purchase_item(item2)
    register.purchase_item(item3)

    # Show items in the cart
    print("Items currently in the cart:")
    register.show_items()

    # Display the total price
    print(f"\nTotal price of items: ${register.get_total():.2f}")

    # Clear the cart
    print("\nClearing the cart...")
    register.clear()

    # Verify the cart is empty
    print("Cart after clearing:")
    register.show_items()

if __name__ == "__main__":
    main()
