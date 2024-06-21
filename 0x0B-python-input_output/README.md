# 0x0B-python-input_output

## Author

Tadala N. Kapengule

## Tasks

### 0. Read file

Write a function that reads a text file (`UTF8`) and prints it to `stdout`:

- __Prototype__: `def read_file(filename=""):`
- You must use the `with` statement
- You don’t need to manage `file permission` or ``file doesn't exist`` exceptions.
- You are __not__ allowed to import any module

__File__
`0-read_file.py`

### 1. Write to a file

Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:

- __Prototype__: `def write_file(filename="", text=""):`
- You must use the `with` statement
- You don’t need to manage ``file permission`` exceptions.
- Your function __should__ create the file if doesn’t exist.
- Your function __should__ overwrite the content of the file if it already exists.
- You are __not__ allowed to import any module

__File__
`1-write_file.py`

### 2. Append to a file

Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:

- __Prototype__: `def append_write(filename="", text=""):`
- If the file doesn’t exist, it __should__ be created
- You must use the `with` statement
- You don’t need to manage ``file permission`` or ``file doesn't exist`` exceptions.
- You are __not__ allowed to import any module

__File__
`2-append_write.py`

### 3. To JSON string

Write a function that returns the `JSON` representation of an object (string):

- __Prototype__: `def to_json_string(my_obj):`
- You don’t need to manage exceptions if the object can’t be serialized.

__File__
`3-to_json_string.py`

### 4. From JSON string to Object

Write a function that returns an object (Python data structure) represented by a `JSON` string:

- __Prototype__: `def from_json_string(my_str):`
- You don’t need to manage exceptions if the `JSON` string doesn’t represent an object.

__File__
`4-from_json_string.py`

### 5. Save Object to a file

Write a function that writes an Object to a text file, using a `JSON` representation:

- __Prototype__: `def save_to_json_file(my_obj, filename):`
- You must use the `with` statement
- You don’t need to manage exceptions if the object can’t be serialized.
- You don’t need to manage `file permission` exceptions.

__File__
`5-save_to_json_file.py`

### 6. Create object from a JSON file

Write a function that creates an Object from a “JSON file”:

- __Prototype__: `def load_from_json_file(filename):`
- You must use the `with` statement
- You don’t need to manage exceptions if the `JSON` string doesn’t represent an object.
- You don’t need to manage file permissions / exceptions.

__File__
`6-load_from_json_file.py`

### 7. Load, add, save

Write a script that adds all arguments to a Python list, and then save them to a file:

- You must use your function `save_to_json_file` from `5-save_to_json_file.py`
- You must use your function `load_from_json_file` from `6-load_from_json_file.py`
- The list must be saved as a `JSON` representation in a file named `add_item.json`
- If the file doesn’t exist, it __should__ be created
- You don’t need to manage file permissions / exceptions.

__File__
`7-add_item.py`

### 8. Class to JSOn

Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for `JSON` serialization of an object:

- __Prototype__: `def class_to_json(obj):`
- `obj` is an instance of a Class
- All attributes of the `obj` Class are serializable: `list`, `dictionary`, `string`, `integer` and `boolean`
- You are __not__ allowed to import any module

__File__
`8-class_to_json.py`

### 9. Student to JSON

Write a class `Student` that defines a student by:

- Public instance attributes:
- - `first_name`
- - `last_name`
- - `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)
- You are __not__ allowed to import any module

__File__
`9-student.py`

### 10. Student to JSON with filter

Write a class `Student` that defines a student by:

- Public instance attributes:
- - `first_name`
- - `last_name`
- - `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):
- - If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
- - Otherwise, all attributes must be retrieved
- You are __not__ allowed to import any module

__File__
`10-student.py`

### 11. Student to disk and reload

Write a class `Student` that defines a student by:

- Public instance attributes:
- - `first_name`
- - `last_name`
- - `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):
- - If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
- - Otherwise, all attributes must be retrieved
- Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:
- - You can assume `json` will always be a dictionary
- - A dictionary key will be the public attribute `name`
- - A dictionary value will be the value of the public attribute
- You are __not__ allowed to import any module

Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation).

__File__
`11-student.py`

### 12. Pascal's triangle

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:

- Returns an empty list if `n <= 0`
- You can assume `n` will be always an integer
- You are __not__ allowed to import any module

__File__
`12-pascal_triangle.py`

### __OPTIONAL <> <> <> TASKS__

### 13. Search and update

Write a function that inserts a line of text to a file, after each line containing a specific string (see example):

- __Prototype__: `def append_after(filename="", search_string="", new_string=""):`
- You must use the `with` statement
- You don’t need to manage `file permission` or `file doesn't exist` exceptions.
- You are __not__ allowed to import any module

__File__
`100-append_after.py`

### 14. Log parsing

Write a script that reads `stdin` line by line and computes metrics:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
- Each 10 lines and after a keyboard interruption (`CTRL + C`), prints those statistics since the beginning:
- - Total file size: File size: `<total size>`
- - where is the sum of all previous (see input format above)
- - Number of lines by status code:
- - - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
- - - if a status code doesn’t appear, don’t print anything for this status code
- - - format: `<status code>`: `<number>`
- - - status codes __should__ be printed in ascending order

```bash
# Usage
./101-generator.py | ./101-stats.py
```

__File__
`101-stats.py`
