# 0x00-python-hello_world

## Author

Tadala N. Kapengule

## Requirements

__Python Scripts__

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3` (version `3.8.5`)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the `pycodestyle` (version `2.8.*`)
- All your files must be **executable**
- The length of your files will be tested using `wc`

__Shell Scripts__

- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on `Ubuntu 20.04 LTS`
- All your scripts should be exactly two lines long (`wc -l` file should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- All your files must be **executable**

__C Scripts__

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on `Ubuntu 20.04 LTS` using `gcc`, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
- All your files should end with a new line
- Your code should use the `Betty `style. It will be checked using `betty-style.pl` and `betty-doc.pl`
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be **include guarded**


## Tasks

### 0. Run Python file

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

__File__
``0-run``, test w ``0-main.py``

### 1. Run inline

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable `$PYCODE`

__File__
``1-run_inline``

### 2. Hello, print

Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

- Use the function `print`

__File__
``2-print.py``

### 3. Print Integer

Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

- You can find the source code here
- The output of the script should be:
	- the number, followed by `Battery street`,
	- followed by a new line
- You are not allowed to cast the variable `number` into a string
- Your code must be 3 lines long
- You have to use f-strings [tips](https://realpython.com/python-f-strings/)

__File__
``3-print_number.py``

### 4. Print float

Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

- You can find the source code here
- The output of the program should be:
	- `Float:`, followed by the `float` with only 2 digits
	- followed by a new line
- You are not allowed to cast `number` to string
- You have to use `f-strings`

__File__
``4-print_float.py``

### 5. Print string

Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

- You can find the source code here
- The output of the program should be:
	- 3 times the value of `str`
	- followed by a new line
	- followed by the 9 first characters of str
	- followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long

__File__
``5-print_string.py``

### 6. Play with strings

Complete this source code to print `Welcome to Holberton School!`

- You can find the source code here
- You are not allowed to use any loops or conditional statements.
- You have to use the variables `str1` and `str2` in your new line of code
- Your program should be exactly 5 lines long

__File__
``6-concat.py``

### 7. Copy - Cut - Paste

Complete this source code

- You can find the source code here
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- `word_first_3` should contain the first 3 letters of the variable word
- `word_last_2` should contain the last 2 letters of the variable word
- `middle_word` should contain the value of the variable word without the first and last letters

__File__

``7-edges.py``

### 8. Create a new sentence

Complete this `source code` to print `object-oriented programming with Python`, followed by a new line.

- You can find the source code `here`
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals

__File__

`8-concat_edges.py`

### 9. Easter egg

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

- Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`).

__File__

`9-easter_egg.py`

### 10. Linked list cycle

*Technical interview preparation*:

- You are not allowed to google anything
- Whiteboard first
- This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.

Write a function in C that checks if a singly linked list has a cycle in it.

- Prototype: `int check_cycle(listint_t *list)`;
- Return: `0` if there is no cycle, `1` if there is a cycle

*Requirements*:

- Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`

`gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle`

__File__

`10-check_cycle.c, lists.h`

___OPTIONAL__ __TASKS__

### 11. Hello, write

Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.

- Use the function `write` from the `sys` module
- You are not allowed to use `print`
- Your script should print to `stderr`
- Your script should exit with the status code `1`

__File__

`100-write.py`

### 12. Compile

Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable `$PYFILE`

The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)

### 13. ByteCode -> Python #1

Write the Python function `def magic_calculation(a, b)`: that does exactly the same as the following Python bytecode:

```bash
 3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```

__File__

`102-magic_calculation.py`