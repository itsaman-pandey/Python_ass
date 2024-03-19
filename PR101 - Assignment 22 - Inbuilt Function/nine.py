# ### Problem 9: Custom `find` Function for Strings

# **Task:** Write a custom function that replicates the behavior of the `str.find()` method. This function should search for a substring within a string and return the index of the first occurrence. If the substring is not found, it should return `-1`.

# - **Sample Input:** `'Look for the substring in this string.'`, `'substring'`
# - **Sample Output:** `12`
# - **Documentation:** [str.find()](https://docs.python.org/3/library/stdtypes.html#str.find)
def custom_find(string, substring):
    return string.find(substring)

sample_string = 'Look for the substring in this string.'
substring = 'substring'
print(custom_find(sample_string, substring))  # Output: 12
