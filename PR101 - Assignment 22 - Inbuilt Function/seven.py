# ### Problem 7: Custom `count` Function

# **Task:** Write a custom function that behaves similarly to Python's `str.count()` and `list.count()` methods. This function should count how many times a specific element appears in a string or a list.

# - **Sample Input (for list):** `[1, 2, 2, 3, 4, 2]`, `2`
# - **Sample Output:** `3`
# - **Sample Input (for string):** `'hello world'`, `'o'`
# - **Sample Output:** `2`
# - **Documentation:** [str.count()](https://docs.python.org/3/library/stdtypes.html#str.count) and [list.count()](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

def custom_count(obj, value):
    if isinstance(obj, str):
        return obj.count(value)
    elif isinstance(obj, list):
        return obj.count(value)
    else:
        raise TypeError("Unsupported type. Expected string or list.")


sample_list = [1, 2, 2, 3, 4, 2]
search_value = 2
print(custom_count(sample_list, search_value)) 