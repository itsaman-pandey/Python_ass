# ### Problem 1: Custom `join` Function

# **Task:** Write a custom function that mimics the behavior of Python's built-in `str.join()` method. This method should take two arguments: a list of strings to be joined and a string separator, and return a single string with each of the list elements joined by the separator.

# - **Sample Input:** `['Hello', 'World']`, `' '`
# - **Sample Output:** `'Hello World'`
# - **Documentation:** [str.join()](https://docs.python.org/3/library/stdtypes.html#str.join)

def join(arr):
    s =''
    for i in arr:
        s = s + i
    return s
l = ['hello','world']
print(join(l))
