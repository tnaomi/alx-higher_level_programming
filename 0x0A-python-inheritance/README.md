# 0x0A-python-inheritance

## Author

Tadala N. Kapengule

## Tasks

### 0. Lookup

Write a function that returns the list of available attributes and methods of an object:

- __Prototype__: `def lookup(obj):`
- Returns a `list` object
- You are __not__ allowed to import any module

__File__
`0-lookup.py`

### 1. My list

Write a class `MyList` that inherits from `list`:

- __Public instance method__: `def print_sorted(self):` that prints the list, but sorted (ascending `sort`)
- You can assume that all the elements of the list will be of type `int`
- You are __not__ allowed to import any module

__File__
`1-my_list.py`, `tests/1-my_list.txt`

### 2. Exact same object

Write a function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`.

- Prototype: `def is_same_class(obj, a_class):`
- You are __not__ allowed to import any module

__File__
`2-is_same_class.py`

### 3. Same class or inherit from

Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.

- __Prototype__: `def is_kind_of_class(obj, a_class):`
- You are __not__ allowed to import any module

__File__
`3-is_kind_of_class.py`

### 4. Only sub class of

Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.

- __Prototype__: `def inherits_from(obj, a_class):`
- You are __not__ allowed to import any module

__File__
`4-inherits_from.py`

### 5. Geometry module

Write an empty class `BaseGeometry`.

- You are __not__ allowed to import any module.

__File__
`5-base_geometry.py`

### 6. Improve geometry

Write a class `BaseGeometry` (based on `5-base_geometry.py`).

- __Public instance method__: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
- You are __not__ allowed to import any module

__File__
`6-base_geometry.py`

### 7. Integer validator

Write a class `BaseGeometry` (based on `6-base_geometry.py`).

- __Public instance method__: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
- __Public instance method__: `def integer_validator(self, name, value):` that validates `value`:
- - you can assume `name` is always a `string`
- - if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
- - if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
- You are __not__ allowed to import any module

__File__
`7-base_geometry.py`, `tests/7-base_geometry.txt`

### 8. Rectangle

Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).

- Instantiation with `width` and `height`: `def __init__(self, width, height):`
- - `width` and `height` must be private. No getter or setter
- - `width` and `height` must be positive integers, validated by `integer_validator`

__File__
`8-rectangle.py`

### 9. Full Rectangle

Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)

- Instantiation with `width` and `height`: `def __init__(self, width, height):`
- - `width` and `height` must be private. No getter or setter
- - `width` and `height` must be positive integers, validated by `integer_validator`

- the `area()` method must be implemented
- `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

__File__
`9-rectangle.py`

### 10. Square #1

Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):

- Instantiation with `size`: `def __init__(self, size):`:
- - `size` must be private. No getter or setter
- - `size` must be a positive integer, validated by `integer_validator`
- the `area()` method must be implemented

__File__
`10-square.py`

### 11. Square #2

Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):

- Instantiation with `size`: `def __init__(self, size):`:
- - `size` must be private. No getter or setter
- - `size` must be a positive integer, validated by `integer_validator`
- the `area()` method must be implemented
- `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`

__File__
`11-square.py`

### __OPTIONAL <> <> TASKS__

### 12. My integer

Write a class `MyInt` that inherits from `int`:

- `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted
- You are __not__ allowed to import any module

__File__
`100-my_int.py`

### 13. Can I?

Write a function that adds a new attribute to an object if it’s possible:

- Raise a `TypeError` exception, with the message `can't add new attribute if the object can’t have new attribute`
- You are __not__ allowed to use `try/except`
- You are __not__ allowed to import any module

__File__
`101-add_attribute.py`
