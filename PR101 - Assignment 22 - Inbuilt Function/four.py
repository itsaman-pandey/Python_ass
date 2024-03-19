# **Task:** Develop a custom function that imitates Python's slicing operation for strings. This function should accept three parameters: the string to slice, the start index, and the end index, returning the corresponding substring.

# - **Sample Input:** `'Hello, World!'`, `7`, `12`
# - **Sample Output:** `'World'`
# - **Documentation:** [Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)

def slice(arr,s,e):
    return arr[s:e]
print(slice('Hello, World!',7,12))