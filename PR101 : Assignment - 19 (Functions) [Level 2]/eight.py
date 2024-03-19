# Write a function named findGCD that takes two integers as input and returns their greatest common divisor (GCD). Use this function to find the GCD of two given numbers.

# gcdResult = findGCD(36, 48);

# // Sample Output: gcdResult = 12

def gcd(m,n):
    a = min(m,n)
    b = max(m,n)
    gcd_n=1
    for i in range(a+1):
        if a%i==0 and b%i==0:
            gcd_n = i
    return gcd_n