#
# Rylee Leavitt
# 3/6/25
# Person and Customer Classes Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program.

# Define the Person class
class Person:
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nTelephone: {self.telephone}"
