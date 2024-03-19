# ### Problem 6: Custom `index` Function for Lists

# **Task:** Create a custom function that mimics the behavior of the `list.index()` method in Python. This function should search a list for a specified value and return the index of the first occurrence. If the value is not found, your function should raise a ValueError.

# - **Sample Input:** `[1, 2, 3, 4, 5]`, `3`
# - **Sample Output:** `2`
# - **Documentation:** [list.index()](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
def custom_index(lst, value):
    for index, element in enumerate(lst):
        if element == value:
            return index
    raise ValueError("Value not found in list")