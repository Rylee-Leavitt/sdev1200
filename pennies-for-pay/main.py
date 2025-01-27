#
# Rylee Leavitt
# 1/26/2025
# Pennies for Pay Programming Project
# SDEV 1200 
#

# Use comments liberally throughout the program.

#function calculate salary
def calculate_salary(days):

    # starts with an empty array
    daily_salaries = []

    #initializes total pay as 0
    total_pay = 0

    #function for time range
    for day in range(days):
        salary = 2 ** day  # Doubling each day
        daily_salaries.append(salary) #appends the salary
        total_pay += salary #adds total pay to the value of the new salary

    # Displaying the salary table and total pay
    print("Day\tSalary ($)")
    print("-" * 18)
    for day in range(days):
        print(f"{day + 1}\t${daily_salaries[day] / 100:.2f}")
    print("-" * 18)
    print(f"Total Pay: ${total_pay / 100:.2f}")

# Asking the user for the number of days
number_of_days = int(input("Enter the number of days: "))
calculate_salary(number_of_days)
