# Custom Python Functions

This repository contains custom Python functions that replicate the behavior of some built-in Python functions.

## Inbuilt Functions

### Problem 1: Custom `join` Function

**Task:** Write a custom function that mimics the behavior of Python's built-in `str.join()` method. This method should take two arguments: a list of strings to be joined and a string separator, and return a single string with each of the list elements joined by the separator.

- **Sample Input:** `['Hello', 'World']`, `' '`
- **Sample Output:** `'Hello World'`
- **Documentation:** [str.join()](https://docs.python.org/3/library/stdtypes.html#str.join)

### Problem 2: Custom `rindex` Function for Lists

**Task:** Create a custom function that behaves like Python's built-in method for finding the last index of an item in a list. If the item is not found, your function should return `-1`.

- **Sample Input:** `[1, 2, 3, 2, 4]`, `2`
- **Sample Output:** `3`
- **Documentation:** There's no direct equivalent in the list methods, but you can refer to [list methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) for inspiration.

### Problem 3: Custom `slice` Function

**Task:** Write a custom function that simulates the behavior of slicing a list in Python. The function should take three parameters: the list to be sliced, the start index, and the end index, and return a new list.

- **Sample Input:** `[1, 2, 3, 4, 5]`, `1`, `4`
- **Sample Output:** `[2, 3, 4]`
- **Documentation:** [Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)

### Problem 4: Custom `substring` Function

**Task:** Develop a custom function that imitates Python's slicing operation for strings. This function should accept three parameters: the string to slice, the start index, and the end index, returning the corresponding substring.

- **Sample Input:** `'Hello, World!'`, `7`, `12`
- **Sample Output:** `'World'`
- **Documentation:** [Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)

### Problem 5: Custom `contains` Function

**Task:** Write a custom function that replicates the behavior of the `in` operator for lists, determining whether a list contains a certain element.

- **Sample Input:** `[1, 2, 3, 4, 5]`, `3`
- **Sample Output:** `True`
- **Documentation:** [Expressions](https://docs.python.org/3/reference/expressions.html#membership-test-operations)

### Problem 6: Custom `index` Function for Lists

**Task:** Create a custom function that mimics the behavior of the `list.index()` method in Python. This function should search a list for a specified value and return the index of the first occurrence. If the value is not found, your function should raise a ValueError.

- **Sample Input:** `[1, 2, 3, 4, 5]`, `3`
- **Sample Output:** `2`
- **Documentation:** [list.index()](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### Problem 7: Custom `count` Function

**Task:** Write a custom function that behaves similarly to Python's `str.count()` and `list.count()` methods. This function should count how many times a specific element appears in a string or a list.

- **Sample Input (for list):** `[1, 2, 2, 3, 4, 2]`, `2`
- **Sample Output:** `3`
- **Sample Input (for string):** `'hello world'`, `'o'`
- **Sample Output:** `2`
- **Documentation:** [str.count()](https://docs.python.org/3/library/stdtypes.html#str.count) and [list.count()](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### Problem 8: Custom `reverse` Function

**Task:** Develop a custom function that reverses the order of items in a list or characters in a string, similar to Python's `reversed()` function or the `[::-1]` slice shortcut.

- **Sample Input (for list):** `[1, 2, 3, 4, 5]`
- **Sample Output:** `[5, 4, 3, 2, 1]`
- **Sample Input (for string):** `'hello'`
- **Sample Output:** `'olleh'`
- **Documentation:** [reversed()](https://docs.python.org/3/library/functions.html#reversed)

### Problem 9: Custom `find` Function for Strings

**Task:** Write a custom function that replicates the behavior of the `str.find()` method. This function should search for a substring within a string and return the index of the first occurrence. If the substring is not found, it should return `-1`.

- **Sample Input:** `'Look for the substring in this string.'`, `'substring'`
- **Sample Output:** `12`
- **Documentation:** [str.find()](https://docs.python.org/3/library/stdtypes.html#str.find)
