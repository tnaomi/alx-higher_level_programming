# 0x08-python-more_classes

## Author

Tadala N. Kapengule

## Tasks

### 0. Simple rectangle

Write an empty class `Rectangle` that defines a rectangle:

- You are **not** allowed to import any module

__File__
`0-rectangle.py`

### 1. Real definition of a rectangle

Write a class `Rectangle` that defines a rectangle by: (based on 0-rectangle.py)

- **Private instance attribute**: `width`:
- - **property** `def width(self):` to retrieve it
- - **property setter** `def width(self, value):` to set it:
- - - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
- - - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- **Private instance attribute**: `height`:
- - **property def** `height(self)`: to retrieve it
- - **property setter** `def height(self, value)`: to set it:
- - - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
- - - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- You are **not** allowed to import any module

__File__
`1-rectangle.py`

### 2. Area and perimeter

Write a class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)

- `Private instance attribute:` `width`:
- - **property** `def width(self):` to retrieve it
- - **property setter** `def width(self, value):` to set it:
- - - `width` must be an integer, otherwise raise a TypeError exception with the message `width must be an integer`
- - - if `width` is less than 0, raise a ValueError exception with the message `width must be >= 0`
- `Private instance attribute:` `height`:
- - **property** `def height(self):` to retrieve it
- - **property setter** `def height(self, value):` to set it:
- - - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
- - - if height is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- **Public instance method**: `def area(self):` that returns the rectangle area
- **Public instance method**: `def perimeter(self):` that returns the rectangle perimeter:
- - if `width` or `height `is equal to `0`, `perimeter` is equal to `0`
- You are **not** allowed to import any module

__File__
`2-rectangle.py`

### 3. String representation

Write a class `Rectangle` that defines a rectangle by: (based on `2-rectangle.py`)

- `Private instance attribute:` `width`:
- - **property** `def width(self):` to retrieve it
- - **property setter** `def width(self, value):` to set it:
- - - `width` must be an integer, otherwise raise a TypeError exception with the message `width must be an integer`
- - - if `width` is less than 0, raise a ValueError exception with the message `width must be >= 0`
- `Private instance attribute:` `height`:
- - **property** `def height(self):` to retrieve it
- - **property setter** `def height(self, value):` to set it:
- - - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
- - - if height is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- **Public instance method**: `def area(self):` that returns the rectangle area
- **Public instance method**: `def perimeter(self):` that returns the rectangle perimeter:
- - if `width` or `height `is equal to `0`, `perimeter` is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
- - if `width` or `height` is equal to `0`, return an empty string

- You are **not** allowed to import any module

__File__
`3-rectangle.py`

### 4. Eval is magic

Write a class `Rectangle` that defines a rectangle by: (based on `3-rectangle.py`)

- `Private instance attribute:` `width`:
- - **property** `def width(self):` to retrieve it
- - **property setter** `def width(self, value):` to set it:
- - - `width` must be an integer, otherwise raise a TypeError exception with the message `width must be an integer`
- - - if `width` is less than 0, raise a ValueError exception with the message `width must be >= 0`
- `Private instance attribute:` `height`:
- - **property** `def height(self):` to retrieve it
- - **property setter** `def height(self, value):` to set it:
- - - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
- - - if height is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- **Public instance method**: `def area(self):` that returns the rectangle area
- **Public instance method**: `def perimeter(self):` that returns the rectangle perimeter:
- - if `width` or `height `is equal to `0`, `perimeter` is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
- - if `width` or `height` is equal to `0`, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)

- You are **not** allowed to import any module

__File__
`4-rectangle.py`

### 5. Detect instance deletion

Write a class `Rectangle` that defines a rectangle by: (based on `4-rectangle.py`)

- `Private instance attribute:` `width`:
- - **property** `def width(self):` to retrieve it
- - **property setter** `def width(self, value):` to set it:
- - - `width` must be an integer, otherwise raise a TypeError exception with the message `width must be an integer`
- - - if `width` is less than 0, raise a ValueError exception with the message `width must be >= 0`
- `Private instance attribute:` `height`:
- - **property** `def height(self):` to retrieve it
- - **property setter** `def height(self, value):` to set it:
- - - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
- - - if height is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- **Public instance method**: `def area(self):` that returns the rectangle area
- **Public instance method**: `def perimeter(self):` that returns the rectangle perimeter:
- - if `width` or `height `is equal to `0`, `perimeter` is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
- - if `width` or `height` is equal to `0`, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of `Rectangle` is deleted

- You are **not** allowed to import any module

__File__
`5-rectangle.py`

### 6. How many instances

Write a class `Rectangle` that defines a rectangle by: (based on `5-rectangle.py`)

- `Private instance attribute:` `width`:
- - **property** `def width(self):` to retrieve it
- - **property setter** `def width(self, value):` to set it:
- - - `width` must be an integer, otherwise raise a TypeError exception with the message `width must be an integer`
- - - if `width` is less than 0, raise a ValueError exception with the message `width must be >= 0`
- `Private instance attribute:` `height`:
- - **property** `def height(self):` to retrieve it
- - **property setter** `def height(self, value):` to set it:
- - - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
- - - if height is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- `Public class attribute` `number_of_instances`:
- - Initialized to `0`
- - Incremented during each new instance instantiation
- - Decremented during each instance deletion
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- **Public instance method**: `def area(self):` that returns the rectangle area
- **Public instance method**: `def perimeter(self):` that returns the rectangle perimeter:
- - if `width` or `height `is equal to `0`, `perimeter` is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
- - if `width` or `height` is equal to `0`, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of `Rectangle` is deleted

- You are **not** allowed to import any module

__File__
`6-rectangle.py`

### 7. Change representation

Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)

- `Private instance attribute:` `width`:
- - **property** `def width(self):` to retrieve it
- - **property setter** `def width(self, value):` to set it:
- - - `width` must be an integer, otherwise raise a TypeError exception with the message `width must be an integer`
- - - if `width` is less than 0, raise a ValueError exception with the message `width must be >= 0`
- `Private instance attribute:` `height`:
- - **property** `def height(self):` to retrieve it
- - **property setter** `def height(self, value):` to set it:
- - - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
- - - if height is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- `Public class attribute` `number_of_instances`:
- - Initialized to `0`
- - Incremented during each new instance instantiation
- - Decremented during each instance deletion
- `Public class attribute` `print_symbol`:
- - Initialized to `#`
- - Used as symbol for string representation
- - Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- **Public instance method**: `def area(self):` that returns the rectangle area
- **Public instance method**: `def perimeter(self):` that returns the rectangle perimeter:
- - if `width` or `height `is equal to `0`, `perimeter` is equal to `0`
- `print()` and `str()` should print the rectangle with the character(s) stored in `print_symbol`:
- - if `width` or `height` is equal to `0`, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of `Rectangle` is deleted

- You are **not** allowed to import any module

__File__
`7-rectangle.py`

### 8. Compare rectangles

Write a class `Rectangle` that defines a rectangle by: (based on `7-rectangle.py`)

- `Private instance attribute:` `width`:
- - **property** `def width(self):` to retrieve it
- - **property setter** `def width(self, value):` to set it:
- - - `width` must be an integer, otherwise raise a TypeError exception with the message `width must be an integer`
- - - if `width` is less than 0, raise a ValueError exception with the message `width must be >= 0`
- `Private instance attribute:` `height`:
- - **property** `def height(self):` to retrieve it
- - **property setter** `def height(self, value):` to set it:
- - - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
- - - if height is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- `Public class attribute` `number_of_instances`:
- - Initialized to `0`
- - Incremented during each new instance instantiation
- - Decremented during each instance deletion
- `Public class attribute` `print_symbol`:
- - Initialized to `#`
- - Used as symbol for string representation
- - Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- **Public instance method**: `def area(self):` that returns the rectangle area
- **Public instance method**: `def perimeter(self):` that returns the rectangle perimeter:
- - if `width` or `height `is equal to `0`, `perimeter` is equal to `0`
- `print()` and `str()` should print the rectangle with the character(s) stored in `print_symbol`:
- - if `width` or `height` is equal to `0`, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the `area`
- - `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
- - `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
- - Returns `rect_1` if both have the same `area` value

- You are **not** allowed to import any module

__File__
`8-rectangle.py`

### 9. A square is a rectangle

Write a class `Rectangle` that defines a rectangle by: (based on `7-rectangle.py`)

- `Private instance attribute:` `width`:
- - **property** `def width(self):` to retrieve it
- - **property setter** `def width(self, value):` to set it:
- - - `width` must be an integer, otherwise raise a TypeError exception with the message `width must be an integer`
- - - if `width` is less than 0, raise a ValueError exception with the message `width must be >= 0`
- `Private instance attribute:` `height`:
- - **property** `def height(self):` to retrieve it
- - **property setter** `def height(self, value):` to set it:
- - - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
- - - if height is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- `Public class attribute` `number_of_instances`:
- - Initialized to `0`
- - Incremented during each new instance instantiation
- - Decremented during each instance deletion
- `Public class attribute` `print_symbol`:
- - Initialized to `#`
- - Used as symbol for string representation
- - Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- **Public instance method**: `def area(self):` that returns the rectangle area
- **Public instance method**: `def perimeter(self):` that returns the rectangle perimeter:
- - if `width` or `height `is equal to `0`, `perimeter` is equal to `0`
- `print()` and `str()` should print the rectangle with the character(s) stored in `print_symbol`:
- - if `width` or `height` is equal to `0`, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the `area`
- - `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
- - `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
- - Returns `rect_1` if both have the same `area` value
- Class method `def square(cls, size=0):` that returns a new `Rectangle` instance with `width == height == size`

- You are **not** allowed to import any module

__OPTIONAL <> <> <> TASKS__

### 10. N queens

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

- **Usage**: `nqueens N`
- - If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status 1
- where N must be an integer greater or equal to 4
- - If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
- - If N is smaller than 4, print `N must be at least 4`, followed by a new line, and exit with the status `1`
- The program should print every possible solution to the problem
- - One solution per line
- - Format: see example
- - You don’t have to print the solutions in a specific order
- You are only allowed to import the `sys` module

__File__
`101-nqueens.py`
