# 
#Rylee Leavitt
# 3/6/25
# Person and Customer Classes Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program.

# Import the Person class
from person import Person

# Define the Customer class as a subclass of Person
class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, on_mailing_list):
        # Initialize attributes from the Person class
        super().__init__(name, address, telephone)
        self.customer_number = customer_number
        self.on_mailing_list = on_mailing_list

    def __str__(self):
        # Include customer-specific details in the string representation
        mailing_list_status = "Yes" if self.on_mailing_list else "No"
        return super().__str__() + f"\nCustomer Number: {self.customer_number}\nOn Mailing List: {mailing_list_status}"
