#
# Rylee Leavitt
# 3/16/25
# Recursive Multiplication Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program. 

# Get user input
def main ():
    # get two numbers
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a second number: '))

    # display their product
    print('Their product is', multiply(num1, num2))

def multiply(x, y):
    # Base case: When y becomes 1, return x
    if x ==0 or y == 0:
        return 0
    else:
        # Recursive case: Add x and call the function with y decremented
        return x + multiply(x, y - 1)

# Call the main function
main ()
