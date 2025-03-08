#
# Rylee
# 3/7/25
# ShiftSupervisor Class Programming Project
# SDEV 1200
#
#Use comments liberally throughout the program.

# shift_supervisor.py
# Import the Employee class
from employee import Employee

# ShiftSupervisor class (inherits from Employee)
class ShiftSupervisor(Employee):
    def __init__(self, name, number, annual_salary, annual_bonus):
        # Call the Employee initializer
        super().__init__(name, number)
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus

    # Accessor methods
    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_bonus(self):
        return self.__annual_bonus

    # Mutator methods
    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus

    # Method to calculate total compensation
    def calculate_total_compensation(self):
        return self.__annual_salary + self.__annual_bonus

    # String representation
    def __str__(self):
        return (f"Shift Supervisor Name: {self.get_name()}, Employee Number: {self.get_number()}, "
                f"Annual Salary: ${self.__annual_salary}, Annual Bonus: ${self.__annual_bonus}, "
                f"Total Compensation: ${self.calculate_total_compensation()}")


# Demonstration program
def main():
    # Create a ShiftSupervisor object
    supervisor = ShiftSupervisor("Astarion Ancunin", "6000", 69000, 10000)

    # Display the ShiftSupervisor's details
    print("Shift Supervisor Details:")
    print(supervisor)

if __name__ == "__main__":
    main()