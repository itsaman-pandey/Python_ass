# ### Problem 3: Custom `slice` Function

# **Task:** Write a custom function that simulates the behavior of slicing a list in Python. The function should take three parameters: the list to be sliced, the start index, and the end index, and return a new list.

# - **Sample Input:** `[1, 2, 3, 4, 5]`, `1`, `4`
# - **Sample Output:** `[2, 3, 4]`
# - **Documentation:** [Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)

# ###

def slice(arr,s,e):
    return arr[s:e]
print(slice([1, 2, 3, 4, 5],1,4))