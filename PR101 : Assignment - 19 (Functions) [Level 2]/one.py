# Write a function named distance that takes the x and y coordinates of two points and returns the distance between them.

# Sample Input: (2, 3), (5, 7);

# Sample Output: 5.0

def dis(x1,y1,x2,y2):
    x = x1-x2
    y = y1 - y2
    d = x**2 + y**2
    d = d ** 0.5
    return d
