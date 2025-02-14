#
# Rylee Leavitt
# 2/9/25
# Pet Class Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

class pet: #defines a new class named pet

    def __init__(self, name, animal_type, age): 
        #function to initialize the pet's attributes
        self.__name = name                  #initializes the pet's name
        self.__animal_type = animal_type    #initializes the pet's type
        self.__age = age                    #initializes the pet's age

    def set_name(self, name): 
        #Function to set a name, parameters of self, name
        self.__name = name #assigns a new value to __name.

    def set_animal_type(self, animal_type):
        #Function to set the type of animal
        self.__animal_type = animal_type #assigns a new value to animal_type

    def set_age(self, age):
        #Function to set the age of the pet
        self.__age = age #assigns a new value to __age

    def get_name(self): #Function to get name
        return self.__name #returns the value of __name.

    def get_animal_type(self): #Function to get type
        return self.__animal_type #returns the value of animal_type

    def get_age(self): #Function to get age
        return self.__age #returns the value of __age

# Program to interact with the Pet class
def main():
    # Prompt the user for pet information
    pet_name = input("Enter the name of your pet: ")
    pet_type = input("Enter the type of animal your pet is (e.g., Dog, Cat, Bird): ")
    pet_age = input("Enter the age of your pet: ")

    # Create a Pet object with the provided information
    pet = pet(pet_name, pet_type, pet_age)

    # Display the pet's information using the accessor methods
    print(f"\nHere is the information about your pet:")
    print(f"Name: {pet.get_name()}")
    print(f"Type: {pet.get_animal_type()}")
    print(f"Age: {pet.get_age()}")

if __name__ == "__main__":
    main()
