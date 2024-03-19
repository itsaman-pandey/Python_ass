# ### Problem 8: Custom `reverse` Function

# **Task:** Develop a custom function that reverses the order of items in a list or characters in a string, similar to Python's `reversed()` function or the `[::-1]` slice shortcut.

# - **Sample Input (for list):** `[1, 2, 3, 4, 5]`
# - **Sample Output:** `[5, 4, 3, 2, 1]`
# - **Sample Input (for string):** `'hello'`
# - **Sample Output:** `'olleh'`
# - **Documentation:** [reversed()](https://docs.python.org/3/library/functions.html#reversed)

def custom_reverse(obj):
    if isinstance(obj, list):
        return obj[::-1]
    elif isinstance(obj, str):
        return obj[::-1]
    else:
        raise TypeError("Unsupported type. Expected string or list.")

sample_list = [1, 2, 3, 4, 5]
print(custom_reverse(sample_list))  
sample_string = 'hello'
print(custom_reverse(sample_string))  
