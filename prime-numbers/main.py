#
# Rylee Leavitt
# 2/5/2025
# Rock, Paper, Scissors Game Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

def is_prime(n): #defines the function
    """Returns True if n is a prime number, otherwise False.""" 
    #docstring """ defines n as an argument & provides a description of the function

    if n <= 1: 
        # if n is less than or equal to 1 it is not a prime number
        return False #If n is <= 1 make the staement false
    
    for i in range(2, int(n ** 0.5) + 1): # For loop that iterates through all possible divisors

        if n % i == 0: #checks if n is divisible by i
            #If the number is divisble other than 1 and itself, it's not a prime number

            return False #Make the statement fales if divisble by any other number
        
    return True #otherwise return true

# Main program
number = int(input("Enter a number: ")) #gets user input
if is_prime(number):  #Identifies if the number is prime
    print(f"{number} is a prime number.") #If numner is prime, prints "(user input)is a prime number."
else:
    print(f"{number} is NOT a prime number.") #otherwise, prints "(user input)is Not a prime number."
