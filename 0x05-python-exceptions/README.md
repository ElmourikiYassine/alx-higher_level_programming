# alx-higher_level_programming

## Description

This repository contains Python scripts that demonstrate the implementation of various tasks related to exception handling.

## Tasks

### Task 0: Safe List Printing

Write a function `safe_print_list` that prints a specified number of elements from a list. The function should handle exceptions using `try` and `except`. The prototype is as follows:

```python
def safe_print_list(my_list=[], x=0):
    pass
```

### Task 1: Safe Printing of Integers

Write a function `safe_print_integer` that prints an integer using the `"{:d}".format()` format. The function should handle exceptions using `try` and `except`. The prototype is as follows:

```python
def safe_print_integer(value):
    pass
```

### Task 2: Print and Count Integers

Write a function `safe_print_list_integers` that prints the first x elements of a list, considering only integers. The function should handle exceptions using `try` and `except`. The prototype is as follows:

```python
def safe_print_list_integers(my_list=[], x=0):
    pass
```

### Task 3: Integers Division with Debug

Write a function `safe_print_division` that divides two integers and prints the result. The function should use `try`, `except`, and `finally` blocks. The prototype is as follows:

```python
def safe_print_division(a, b):
    pass
```

### Task 4: Divide a List

Write a function `list_division` that divides element by element two lists. The function should use `try`, `except`, and `finally` blocks. The prototype is as follows:

```python
def list_division(my_list_1, my_list_2, list_length):
    pass
```

### Task 5: Raise Exception

Write a function `raise_exception` that raises a type exception. The prototype is as follows:

```python
def raise_exception():
    pass
```

### Task 6: Raise a Message

Write a function `raise_exception_msg` that raises a name exception with a message. The prototype is as follows:

```python
def raise_exception_msg(message=""):
    pass
```

### Task 7: Safe Integer Print with Error Message (Advanced)

Write a function `safe_print_integer_err` that prints an integer and returns True if the value is an integer, otherwise returns False. The function should also print an error message to stderr in case of an exception. The prototype is as follows:

```python
def safe_print_integer_err(value):
    pass
```

### Task 8: Safe Function (Advanced)

Write a function `safe_function` that executes a function safely and returns the result. The function should use `try` and `except` blocks. The prototype is as follows:

```python
def safe_function(fct, *args):
    pass
```

### Task 9: ByteCode -> Python #4 (Advanced)

Write a Python function `magic_calculation` that replicates a given Python bytecode. The prototype is as follows:

```python
def magic_calculation(a, b):
    pass
```

### Task 10: CPython #2: PyFloatObject (Advanced)

Create three C functions that print basic information about Python lists, Python bytes, and Python float objects. The functions should handle errors and print relevant information. The prototypes are as follows:

```c
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
```

## Requirements

- All scripts should be written in Python.
- C functions should be compiled using the provided compilation command.
- The Python scripts should be executable and print the expected output.

## Author

[Yassine El mouriki]

**GitHub Repository:** [alx-higher_level_programming](https://github.com/ElmourikiYassine/alx-higher_level_programming)

**Directory:** 0x05-python-exceptions
