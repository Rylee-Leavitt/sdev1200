#
# Rylee Leavitt
# 2/17/25
# Cash Register Programming Project
# SDEV 1200
#

#Main py
from cash_Register import CashRegister
def main():

    # Display the items and the total
    print("Items purchased:")
    CashRegister.show_items()
    print(f"\nTotal price: ${CashRegister.get_total():.2f}")

if __name__ == "__main__":
    main()