# 0x06-python-classes

## Author

Tadala N. Kapengule

## Tasks

### 0. My first square

Write an empty class `Square` that defines a square:

- You are **not** allowed to import any module

__File__

`0-square.py`

### 1. Square with size

Write a class `Square` that defines a square by: (based on `0-square.py`)

- **Private instance attribute**: `size`
- Instantiation with `size` (no type/value verification)
- You are **not** allowed to import any module

__Why?__

Why size is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

__File__

`1-square.py`

### 2. Size validation

Write a class `Square` that defines a square by: (based on `1-square.py`)

- `Private instance attribute`: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
- - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- You are **not** allowed to import any module

__File__

`2-square.py`

### 3. Area of a square

Write a class `Square` that defines a square by: (based on `2-square.py`)

- **Private instance attribute**: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
- - if size is less than 0, raise a ValueError exception with the message `size must be >= 0`
- **Public instance method**: `def area(self):` that returns the current square area
- You are **not** allowed to import any module

__File__

`3-square.py`

### 4. Access and update private attribute

Write a class `Square` that defines a square by: (based on `3-square.py`)

- **Private instance attribute**: `size`:
- - property `def size(self):` to retrieve it
- - property setter `def size(self, value):` to set it:
- - - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
- - - if `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- **Public instance method**: `def area(self):` that returns the current square area
- You are **not** allowed to import any module

__Why?__

Why a getter and setter?

Reminder: `size` is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

__File__

`4-square.py`

### 5. Printing a square

Write a class ``Square`` that defines a square by: (based on `4-square.py`)

- **Private instance attribute**: `size`:
- - property `def size(self):` to retrieve it
- - property setter `def size(self, value):` to set it:
- - - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
- - - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- **Public instance method**: `def area(self):` that returns the current square area
- **Public instance method**: `def my_print(self):` that prints in stdout the square with the character #:
- - if `size` is equal to `0`, print an empty line
- You are **not** allowed to import any module

__File__

`5-square.py`

### 6. Coordinates of a square

Write a class `Square` that defines a square by: (based on `5-square.py`)

- **Private instance attribute**: `size`:
- - property `def size(self):` to retrieve it
- - property setter `def size(self, value):` to set it:
- - - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
- - - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- **Private instance attribute**: `position`:
- - property `def position(self):` to retrieve it
- - property setter `def position(self, value):` to set it:
- - - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
- Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
- **Public instance method**: `def area(self):` that returns the current square area
- **Public instance method**: `def my_print(self):` that prints in stdout the square with the character #:
- - if `size` is equal to `0`, print an empty line
- - `position` should be use by using space - Don’t fill lines by spaces when `position[1]` > `0`
- You are **not** allowed to import any module


__File__

`6-square.py`

__OPTIONAL <> <> <> TASKS__

### 7. Singly linked list

Write a class `Node` that defines a node of a singly linked list by:

- **Private instance attribute**: `data`:
- -  property `def data(self):` to retrieve it
- -  property setter `def data(self, value):` to set it:
- - -  `data` must be an integer, otherwise raise a `TypeError` exception with the message `data must be an integer`
- **Private instance attribute**: next_node:
- -  property `def next_node(self):` to retrieve it
- -  property setter `def next_node(self, value):` to set it:
- - -  `next_node` can be `None` or must be a Node, otherwise raise a `TypeError` exception with the message `next_node must be a Node object`
- Instantiation with `data` and `next_node`: `def __init__(self, data, next_node=None):`

And, write a class `SinglyLinkedList` that defines a singly linked list by:

- **Private instance attribute**: `head` (no setter or getter)
- **Simple instantiation**: `def __init__(self):`
- Should be printable:
- -  print the entire list in stdout
- -  one node number by line
- **Public instance method**: `def sorted_insert(self, value):` that inserts a new Node into the correct sorted position in the list (increasing order)
- You are **not** allowed to import any module

__File__

`100-singly_linked_list.py`

### 8. Print Square instance

Write a class `Square` that defines a square by: (based on `6-square.py`)

- **Private instance attribute**: `size:`
- -  property `def size(self):` to retrieve it
- -  property setter `def size(self, value):` to set it:
- - -  `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
- - -  if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- **Private instance attribute**: `position:`
- -  property `def position(self):` to retrieve it
- -  property setter `def position(self, value):` to set it:
- - -  `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integer`
- Instantiation with optional size and optional position: `def __init__(self, size=0, position=(0, 0)):`
- **Public instance method**: `def area(self):` that returns the current square area
- **Public instance method**: `def my_print(self):` that prints in `stdout` the square with the character #:
- -  if `size` is equal to `0`, print an empty line
- -  `position` should be use by using space
- Printing a Square instance should have the same behavior as `my_print()`
- You are **not** allowed to import any module

__File__

`101-square.py`

### 9. Compare 2 squares

Write a class `Square` that defines a square by: (based on `4-square.py`)

- **Private instance attribute**: `size:`
- -  property `def size(self)`: to retrieve it
- -  property setter `def size(self, value)`: to set it:
- - -  size must be a number (float or integer), otherwise raise a TypeError exception with the message `size must be a number`
- - -  if size is less than 0, raise a ValueError exception with the message `size must be >= 0`
- Instantiation with size: `def __init__(self, size=0):`
- **Public instance method**: `def area(self):` that returns the current square area
- `Square` instance can answer to comparators: `==`, `!=`, `>`, `>=`, `<` and `<=` based on the square area
- You are **not** allowed to import any module

__File__

`102-square.py`

### 10. ByteCode -> Python #5

Write the Python class `MagicClass` using ByteCode.

__File__

`103-magic_class.py`