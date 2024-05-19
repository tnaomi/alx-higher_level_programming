# 0x04. Python - More Data Structures: Set, Dictionary

## Authors

Tadala N. Kapengule

## Objectives

- What are sets and how to use them
- What are the most common methods of set and how to use them
- When to use *sets* versus *lists*
- How to iterate into a set
- What are *dictionaries* and how to use them
- When to use dictionaries versus lists or sets
- What is a key in a dictionary
- How to iterate over a dictionary
- What is a `lambda` function
- What are the `map`, `reduce` and `filter` functions

## Tasks

### 0. Squared simple

Write a function that computes the square value of all integers of a matrix.

- **Prototype**: `def square_matrix_simple(matrix=[]):`
- `matrix` is a 2 dimensional array
- Returns a new matrix:
- - Same size as matrix
- - Each value should be the square of the value of the input
- Initial matrix should __not__ be modified
- You are __not__ allowed to import any module
- You are allowed to use regular loops, map, etc.

__File__

`0-square_matrix_simple.py`

### 1. Search and replace

Write a function that _replaces all occurrences of an element_ by another in a new list.

- **Prototype**: `def search_replace(my_list, search, replace):`
- `my_list` is the initial list
- `search` is the element to replace in the list
- `replace` is the new element
- You are __not__ allowed to import any module

__File__

`1-search_replace.py`

### 2. Unique addition

Write a function that _adds all unique integers_ in a list (only once for each integer).

- **Prototype**: `def uniq_add(my_list=[]):`
- You are __not__ allowed to import any module

__File__

`2-uniq_add.py`

### 3. Present in both

Write a function that returns a set of common elements in two sets.

- **Prototype**: `def common_elements(set_1, set_2):`
- You are __not__ allowed to import any module

__File__

`3-common_elements.py`

### 4. Only differents

Write a function that *returns a set of all elements* present in *only one* set.

- **Prototype**: `def only_diff_elements(set_1, set_2):`
- You are __not__ allowed to import any module

__File__

`4-only_diff_elements.py`

### 5. Number of keys

Write a function that returns the *number of keys* in a dictionary.

- **Prototype**: `def number_keys(a_dictionary):`
- You are __not__ allowed to import any module

__File__

`5-number_keys.py`

### 6. Print sorted dictionary

Write a function that *prints* a dictionary *by ordered keys*.

- **Prototype**: `def print_sorted_dictionary(a_dictionary):`
- You can assume that all keys are strings
- Keys should be sorted by alphabetic order
- Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
- Dictionary values can have any type
- You are __not__ allowed to import any module


__File__

`6-print_sorted_dictionary.py`

### 7. Update dictionary

Write a function that *replaces or adds key/value* in a dictionary.

- **Prototype**: `def update_dictionary(a_dictionary, key, value):`
- `key` argument will be always a string
- `value` argument will be any type
- If a key exists in the dictionary, the value will be replaced
- If a key doesn’t exist in the dictionary, it will be created
- You are __not__ allowed to import any module


__File__

`7-update_dictionary.py`

### 8. Simple delete by key

Write a function that *deletes a key* in a dictionary.

- **Prototype**: `def simple_delete(a_dictionary, key=""):`
- `key` argument will be always a string
- If a key doesn’t exist, the dictionary won’t change
- You are __not__ allowed to import any module

__File__

`8-simple_delete.py`

### 9. Multiply by 2

Write a function that returns a *new dictionary* with *all values multiplied by 2*

- **Prototype**: `def multiply_by_2(a_dictionary):`
- You can assume that all values are only integers
- Returns a new dictionary
- You are __not__ allowed to import any module


__File__

`9-multiply_by_2.py`

### 10. Best Score

Write a function that returns a *key* with the *biggest integer value*.

- **Prototype**: `def best_score(a_dictionary):`
- You can assume that all values are only integers
- If no score found, return `None`
- You can assume all students have a different score
- You are __not__ allowed to import any module

__File__

`10-best_score.py`

### 11. Multiply by using map

Write a function that returns a list with all values multiplied by a number without using any loops.

- **Prototype**: `def multiply_list_map(my_list=[], number=0):`
- Returns a new list:
- - Same length as `my_list`
- - Each value should be multiplied by number
- Initial list should __not__ be modified
- You are __not__ allowed to import any module
- You have to use `map`
- Your file should be max 3 lines

__File__

`11-multiply_list_map.py`

### 12. Roman to Integer

Create a function `def roman_to_int(roman_string):` that converts a Roman numeral to an integer.

- You can assume the number will be between 1 to 3999.
- `def roman_to_int(roman_string)` must return an integer
- If the `roman_string` is not a string or `None`, return `0`

__File__

`12-roman_to_int.py`

__OPTIONAL <> <> <> TASKS__

### 13. Weighted average!

Write a function that returns the `weighted average` of all integers tuple `(<score>, <weight>)`

- **Prototype**: `def weight_average(my_list=[]):`
- Returns `0` if the list is empty
- You are __not__ allowed to import any module

__File__

`100-weight_average.py`

### 14. Squared by using map

Write a function that computes the square value of all integers of a matrix using map

- **Prototype**: `def square_matrix_map(matrix=[]):`
- `matrix` is a 2 dimensional array
- Returns a new matrix:
- - Same size as `matrix`
- - Each value should be the square of the value of the input
- Initial `matrix` should __not__ be modified
- You are __not__ allowed to import any module
- You have to use `map`
- You are not allowed to use `for` or `while`
- Your file should be max 3 lines

`101-square_matrix_map.py`

### 15. Delete by value

Write a function that _deletes keys_ with a _specific value_ in a dictionary.

- **Prototype**: `def complex_delete(a_dictionary, value):`
- If the value doesn’t exist, the dictionary won’t change
- _All_ keys having the searched value have to be deleted
- You are __not__ allowed to import any module

`102-complex_delete.py`

### 16. CPython #1: PyBytesObject

Create two C functions that print some basic info about Python lists and Python bytes objects.

**Python lists**:

- **Prototype**: `void print_python_list(PyObject *p);`
- Format: see example

**Python bytes**:

- **Prototype**: `void print_python_bytes(PyObject *p);`
- Format: see example
- Line “first X bytes”: print a maximum of 10 bytes
- If `p` is not a valid PyBytesObject, print an error message (see example)
- Read `/usr/include/python3.4/bytesobject.h`

**About**:

- Python version: `3.4`
- Your shared library will be compiled with this command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c`
- You are not allowed to use the following macros/functions:
-     
```bash
Py_SIZE
Py_TYPE
PyList_GetItem
PyBytes_AS_STRING
PyBytes_GET_SIZE
```
__File__

`103-python.c`