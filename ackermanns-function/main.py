#
# Rylee Leavitt
# 3/16/25
# Ackermann's Function Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

def ackermann(m, n):
    # Ackermann's Function is a recursive mathematical algorithm 
    # that can be used to test how well a system optimizes its performance of recursion.
    
    # Base case: If m equals 0, return n + 1
    if m == 0:
        return n + 1
    
    # If n = 0 then return ackermann(m - 1, 1) 
    elif n == 0:
        return ackermann(m - 1, 1)
    
    # Otherwise, return ackermann(m - 1, ackermann(m, n - 1))`
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# Testing the function with small values for m and n
# Test 1: 
# When both m and n are 0, the base case should trigger
print(ackermann(0, 0))  # Expected output: 1

# Test 2:
print(ackermann(2, 1))  # Expected output: 5

# Test 3:
print(ackermann(2, 2))  # Expected output: 7

#Test 4:
print(ackermann(2, 3))  # Expected output: 9