# 0x01-python-if_else_loops_functions

## Author

Tadala N. Kapengule

## Tasks

### 0. Positive anything is better than negative nothing

This program will assign a random signed `number` to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.

- You can find the source code here
- The variable number will store a different value every time you will run this program
- You don’t have to understand what `import`, `random.randint` do. Please do not touch this code. This line should not change: `number = random.randint(-10000, 10000)`
- The output of the program should be:
	- The number, followed by
		- if the number is greater than 0: `is positive`
		- if the number is 0: `is zero`
		- if the number is less than 0: `is negative`
	- followed by a new line


__File__

`0-positive_or_negative.py`

### 1. The last digit

This program will assign a random signed `number` to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.

- You can find the source code here
- The variable number will store a different value every time you will run this program
- You don’t have to understand what `import`, `random.randint` do. Please do not touch this code. This line should not change: `number = random.randint(-10000, 10000)`
- The output of the program should be:
	- The string Last digit of, followed by
	- the number, followed by
	- the string is, followed by the last digit of number, followed by
		-  if the last digit is greater than 5: the string and is greater than 5
		-  if the last digit is 0: the string and is 0
		-  if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
	- followed by a new line

__File__

`1-last_digit.py`

### 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

__File__

`2-print_alphabet.py`

### 3. When I was having that alphabet soup, I never thought that it would pay off

Write a program that prints the `ASCII` alphabet, in lowercase, not followed by a new line.

- Print all the letters except `q` and `e`
- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

__File__

`3-print_alphabt.py`

### 4. Hexadecimal printing

Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal (as in the following example)

- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

__File__

`4-print_hexa.py`

### 5. 00...99 

Write a program that prints numbers from `0` to `99`.

- Numbers must be separated by `,`, followed by a `space`
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 2 print functions with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

__File__

`5-print_comb2.py`

### 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need

Write a program that prints all possible different combinations of two digits.

- Numbers must be separated by `,`, followed by a space
- The two digits must be different
- `01` and `10` are considered the same combination of the two digits 0 and 1
- Print only the smallest combination of two digits
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 3 print functions with string format
- You can only use no more than 2 loops in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

__File__

`6-print_comb3.py`

### 7. islower

Write a function that checks for lowercase character.

- *Prototype*: `def islower(c)`:
- Returns True if `c` is lowercase
- Returns False otherwise
- You are not allowed to import any module
- You are not allowed to use `str.upper()` and `str.isupper()`
- Tips: [ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)

You don’t need to understand `__import__`

__File__

`7-islower.py`

### 8. To uppercase

Write a function that prints a string in uppercase followed by a new line.

- *Prototype*: `def uppercase(str)`:
- You can only use no more than 2 `print` functions with string format
- You can only use one loop in your code
- You are not allowed to import any module
- You are not allowed to use `str.upper()` and `str.isupper()`
- Tips: [ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)

You don’t need to understand `__import__`

__File__

`8-uppercase.py`

### 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important

Write a function that prints the last digit of a number.

- *Prototype*: `def print_last_digit(number)`:
- Returns the value of the last digit
- You are not allowed to import any module

You don’t need to understand `__import__`

__File__

`9-print_last_digit.py`

### 10. a + b

Write a function that adds two integers and returns the result.

- *Prototype*: `def add(a, b):`
- Returns the value of `a + b`
- You are not allowed to import any module

You don’t need to understand `__import__`

__File__

`10-add.py`

### 11. a ^ b

Write a function that computes `a` to the power of `b` and return the value.

- Prototype: `def pow(a, b):`
- Returns the value of `a ^ b`
- You are not allowed to import any module

You don’t need to understand `__import__`

__File__

`11-pow.py`

### 12. Fizz Buzz

Write a function that prints the numbers from 1 to 100 separated by a space.

- For multiples of three print `Fizz` instead of the number and for multiples of five print `Buzz`.
- For numbers which are multiples of both three and five print `FizzBuzz`.
- *Prototype*: `def fizzbuzz()`:
- Each element should be followed by a space
- You are not allowed to import any module

You don’t need to understand `__import__`

__File__

`12-fizzbuzz.py`

### 13. Insert in sorted linked list

Write a function in C that inserts a number into a sorted singly linked list.

- Prototype: `listint_t *insert_node(listint_t **head, int number);`
- Return: the address of the new node, or `NULL` if it failed

```bash
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 13-main.c linked_lists.c 13-insert_number.c -o insert
```
__File__

`13-insert_number.c`, `lists.h`

__OPTIONAL__ __TASKS__

### 14. Smile in the mirror

Write a program that prints the `ASCII` alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and `Y` in uppercase) , not followed by a new line.

- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

__File__

`100-print_tebahpla.py`

### 15. Remove at position

Write a function that creates a copy of the string, removing the character at the position `n` (not the Python way, the “C array index”).

- Prototype: `def remove_char_at(str, n):`
- You are not allowed to import any module

You don’t need to understand `__import__`

__File__

`101-remove_char_at.py`

### 16. ByteCode -> Python #2

Write the Python function `def magic_calculation(a, b, c):` to function as a bytecode.

__File__

`102-magic_calculation.py`