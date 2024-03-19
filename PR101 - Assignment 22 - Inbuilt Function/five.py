

# ### Problem 5: Custom `contains` Function

# **Task:** Write a custom function that replicates the behavior of the `in` operator for lists, determining whether a list contains a certain element.

# - **Sample Input:** `[1, 2, 3, 4, 5]`, `3`
# - **Sample Output:** `True`
# - **Documentation:** [Expressions](https://docs.python.org/3/reference/expressions.html#membership-test-operations)
def custom_contains(lst, value):
    return value in lst

sample_list = [1, 2, 3, 4, 5]
search_value = 3
print(custom_contains(sample_list, search_value))  
