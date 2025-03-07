#
# Name
# Date
# Person and Customer Classes Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.

import person

# Main function
def main():
    # Get data attributes from the user
    name = input("Enter the customer's name: ")
    address = input("Enter the customer's address: ")
    telephone = input("Enter the customer's telephone number: ")
    customer_number = input("Enter the customer's number: ")
    on_mailing_list = input("Is the customer on the mailing list? (yes/no): ").lower() == 'yes'

    # Create an instance of Customer
    customer = Customer(name, address, telephone, customer_number, on_mailing_list)
    
    # Display information
    print(customer.display())

# Call the main function
if __name__ == "__main__":
    main()