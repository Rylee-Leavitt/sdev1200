#
# Rylee Leavitt
# 2/24/25
# Employee And ProductionWorker Classes Programming Project
# SDEV 1200
#

# employee.py
class Employee:
    def __init__(self, name, number): #initializes employee name and number
        self.__name = name 
        #assigns the value of the parameter self.__name to the instance variable name

        self.__number = number
        #assigns the value of the parameter self.__number to the instance variable number

    # Accessor methods
    def get_name(self): #returns the employee name
        return self.__name

    def get_number(self): #returns the employee number
        return self.__number

    # Mutator methods
    def set_name(self, name): #sets self._name = name
        self.__name = name

    def set_number(self, number):#sets self._number = number
        self.__number = number
