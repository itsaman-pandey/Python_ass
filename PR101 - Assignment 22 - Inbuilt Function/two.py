# ### Problem 2: Custom `rindex` Function for Lists

# **Task:** Create a custom function that behaves like Python's built-in method for finding the last index of an item in a list. If the item is not found, your function should return `-1`.

# - **Sample Input:** `[1, 2, 3, 2, 4]`, `2`
# - **Sample Output:** `3`
# - **Documentation:** There's no direct equivalent in the list methods, but you can refer to [list methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) for inspiration.

def rindex(arr,val):
    for i,j in enumerate(arr[::-1]):
        if j==val:
            return len(arr)-i-1
    else:
        return -1
arr = [1,2,3,2,4]
print(rindex(arr,4))
        