# Factorial Calculation

# Write a function named calculateFactorial that takes an integer n as input and returns the factorial of n (n!). Use this function to calculate the factorial of a given number.

# result = calculateFactorial(5);

# // Sample Output: result = 120
def calculatedFactorila(n):
    if n <= 1:
        return 1
    return n*calculatedFactorila(n-1)
print(calculatedFactorila(5))