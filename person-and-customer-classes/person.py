#
# Rylee Leavitt
# 2/24/25
# Person and Customer Classes Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.

# Define the Person class
class Person:
    def __init__(self, name, address, telephone):
        self.name, address, and telephone
        self.name = name
        self.address = address
        self.telephone = telephone

    def display(self):
        return f"Name: {self.name}\nAddress: {self.address}\nTelephone: {self.telephone}"

# Define the Customer class as a subclass of Person
class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, on_mailing_list):
        super().__init__(name, address, telephone)
        self.customer_number = customer_number
        self.on_mailing_list = on_mailing_list

    def display(self):
        return (super().display() + 
                f"\nCustomer Number: {self.customer_number}" +
                f"\nOn Mailing List: {self.on_mailing_list}")
    