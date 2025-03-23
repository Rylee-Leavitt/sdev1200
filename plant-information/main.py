#
# Rylee Leavitt
# 1/9/25
# Plant Information Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

# Base class: Plant
# Define the Plant Class
class Plant:
    def __init__(self, name, cost):
        # Initializes the object's name and cost attributes when a Plant instance is created.

        self.name = name #assigns self(plant).name the alias name
        self.cost = cost #assigns self(plant).cost the alias cost

    def print_info(self):
        # displays the information about the plant

        print(f"Plant Information: ")   # displays: Plant information:
        print(f"   Plant Name: {self.name}") # displays: Plant Name: (name of the plant)
        print(f"   Cost: {self.cost}")  # displays: Cost: (Cost of the plant)

# Define the derived Flower Class (Inherits from Plant)
class Flower(Plant):
    def __init__(self, name, cost, annual, color):
        # Initialize the Flower object by calling the Plant constructor

        super().__init__(name, cost)
        #calls the parent Plant class to initialize common attributes (name and cost)
        # Additional attributes specific to the Flower class
        
        # Extends the Plant class by adding attributes annual and color.
        self.annual = annual #self(flower).annual the alias annual
        self.color = color #self(flower).color the alias color

    def print_info(self):
        # overrides the parent class's version 
        # to also print information about the annual status and color of the flower.

        print(f"Plant Information:") # displays: Plant information:
        print(f"   Plant name: {self.name}")  # displays: Plant Name: (name of the plant)
        print(f"   Cost: {self.cost}") # displays: Cost: (Cost of the plant)
        print(f"   Annual: {self.annual}") # displays: Annual: (wether or not it is annual)
        print(f"   Color of flowers: {self.color}") # displays: Color of flowers: (flower color)

# Function to print all elements in the my_garden list
def print_list(my_garden):
    # Iterate through the list and print information for each object

    for i, plant in enumerate(my_garden, start=1):
        # loops through each object in the my_garden list.
        # for each object, print an entry number
        # and call the respective object's print_info() method

        print(f"Plant {i} Information:") # prints: Plant (entry number) Information:
        plant.print_info() # displays info
        print()  # add a blank line for better formatting between entries

# Main logic to read input and populate the list
my_garden = []  # Initialize an Empty List (my_garden) to store Plant and Flower objects

while True:
    #Input Loop to Populate the List

    # Prompt the user to specify the type of item or quit
    item_type = input("Enter 'plant' or 'flower' to add an item to the garden (or '-1' to finish): ")
    if item_type == "-1":
        break  # Exit the loop if the user enters '-1'
    
    if item_type == "plant":
        # Ask for plant-specific details

        name = input("Enter the plant name: ") #asks for the plants name
        cost = float(input("Enter the cost of the plant: ")) #asks for the cost of the plant

        # Create a Plant object and add it to the list
        my_garden.append(Plant(name, cost))

    elif item_type == "flower":
        # Ask for flower-specific details
        name = input("Enter the flower name: ") #asks for the flowers name
        cost = float(input("Enter the cost of the flower: ")) #asks for the cost of the flower
        annual = input("Is the flower annual? (true/false): ").lower() == "true"  # Convert input to boolean; true or false
        color = input("Enter the color of the flower: ") #asks for the color of the flower

        # Create a Flower object and add it to the list
        my_garden.append(Flower(name, cost, annual, color))

    else:
        # Handle invalid input
        print("Invalid input. Please enter 'plant', 'flower', or '-1'.")

# Print all elements in the listprint_list(my_garden)
print_list(my_garden) # Output Results
