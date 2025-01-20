#
# Rylee Leavitt
# 1/19/25
# Ingredient Adjuster Programming Project
# SDEV 1200 

# Use comments liberally throughout the program.

# Declare variables.
# the ingredients for 48 cookies
sugar = 1.5
butter = 1
flour = 2.75
total_cookies = 48

# Ask the user how many cookies they want to make
desired_cookies = int(input("Enter the number of cookies you want to make: "))

# Calculate the amount of each ingredient needed
required_sugar = (sugar / total_cookies) * desired_cookies
required_butter = (butter / total_cookies) * desired_cookies
required_flour = (flour / total_cookies) * desired_cookies

# Display the results formatted to two decimal points
print(f"To make {desired_cookies} cookies, you will need:")
print(f"{required_sugar:.2f} cups of sugar")
print(f"{required_butter:.2f} cups of butter")
print(f"{required_flour:.2f} cups of flour")
