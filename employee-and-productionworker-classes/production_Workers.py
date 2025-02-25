#
# Rylee Leavitt
# 2/24/25
# Employee And ProductionWorker Classes Programming Project
# SDEV 1200
#

# production_Worker.py

from employee import Employee

class Production_Worker(Employee): #Defines the Production_Worker class with the parameter of employee

    def __init__(self, name, number, shift, pay_rate): #initializes the value 
        super().__init__(name, number)
        #superclass (Employee). 
        #allows the subclass (ProductionWorker) to inherit and properly initialize the attributes of the superclass.

        self.__shift = shift
        #assigns the value of the parameter self.__shift to the instance variable shift

        self.__pay_rate = pay_rate
        #assigns the value of the parameter self.__pay_rate to the instance variable pay_rate

    # Accessor methods
    def get_shift(self): #returns the employee shift
        return self.__shift

    def get_pay_rate(self): #returns the employee pay rate
        return self.__pay_rate

    # Mutator methods
    def set_shift(self, shift): #sets self.__shift = shift
        self.__shift = shift

    def set_pay_rate(self, pay_rate): #sets self.__pay_rate = pay_rate
        self.__pay_rate = pay_rate
