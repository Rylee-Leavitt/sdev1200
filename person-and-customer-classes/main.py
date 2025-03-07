#
# Rylee Leavitt
# 3/6/25
# Person and Customer Classes Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.
# Import the Customer class
from customer import Customer

# Demonstration program
def main():
    # Create an instance of the Customer class
    customer = Customer(
        name="Astarion Ancunin",
        address="Lower City, Baldur's Gate",
        telephone="666-6666",
        customer_number=1001,
        on_mailing_list=True
    )

    # Display the customer details
    print(customer)

if __name__ == "__main__":
    main()
