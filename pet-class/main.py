#
# Rylee Leavitt
# 2/9/25
# Pet Class Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

import pet

def main():
    # Function to prompt the user for pet information
    pet_name = input("Enter the name of your pet: ") #asks user for pet name
    pet_type = input("Enter the type of animal your pet is (e.g., Dog, Cat, Bird): ") #asks user for animal type
    pet_age = input("Enter the age of your pet: ") #asks user for animal age

    # Create a Pet object with the provided information
    pet = pet(pet_name, pet_type, pet_age)

    # Display the pet's information using the accessor methods
    print(f"\nHere is the information about your pet:") #prints Here is the information about your pet:
    print(f"Name: {pet.get_name()}")
    print(f"Type: {pet.get_animal_type()}")
    print(f"Age: {pet.get_age()}")

if __name__ == "__main__":
    main() #calls the main function
