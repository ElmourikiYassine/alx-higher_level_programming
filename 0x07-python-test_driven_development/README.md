# alx-higher_level_programming

## 0x07-python-test_driven_development

This repository contains Python scripts that demonstrate test-driven development (TDD) principles. Each script corresponds to a specific task and includes both the script file and its associated test file.

### Task 0: Integers Addition

- **File:** `0-add_integer.py`
- **Description:**
  - Implements a function that adds two integers.
  - Raises a `TypeError` exception if either input is not an integer or a float.
  - Returns the sum as an integer.
  - No module imports allowed.

### Task 1: Divide a Matrix

- **File:** `2-matrix_divided.py`
- **Description:**
  - Implements a function that divides all elements of a matrix.
  - Raises `TypeError` exceptions for invalid inputs.
  - Returns a new matrix with elements rounded to 2 decimal places.
  - No module imports allowed.

### Task 2: Say My Name

- **File:** `3-say_my_name.py`
- **Description:**
  - Implements a function that prints "My name is \<first name\> \<last name\>".
  - Raises `TypeError` exceptions for invalid inputs.
  - No module imports allowed.

### Task 3: Print Square

- **File:** `4-print_square.py`
- **Description:**
  - Implements a function that prints a square with the character `#`.
  - Raises `TypeError` and `ValueError` exceptions for invalid inputs.
  - No module imports allowed.

### Task 4: Text Indentation

- **File:** `5-text_indentation.py`
- **Description:**
  - Implements a function that prints a text with 2 new lines after each '.', '?', and ':' characters.
  - Raises a `TypeError` exception for invalid inputs.
  - No module imports allowed.

### Task 5: Max Integer - Unittest

- **File:** `6-max_integer.py`
- **Description:**
  - Implements a function to find and return the max integer in a list.
  - Includes a corresponding unittest file (`tests/6-max_integer_test.py`).
  - Must be executed using `python3 -m unittest tests.6-max_integer_test`.
  - Encouraged collaborative test case creation.

### Task 6: Matrix Multiplication

- **File:** `100-matrix_mul.py`
- **Description:**
  - Implements a function that multiplies two matrices.
  - Raises `TypeError` and `ValueError` exceptions for invalid inputs.
  - No module imports allowed.

### Task 7: Lazy Matrix Multiplication

- **File:** `101-lazy_matrix_mul.py`
- **Description:**
  - Implements a function that multiplies two matrices using the NumPy module.
  - Raises new exception types and messages.
  - Test cases are the same as in `100-matrix_mul`.
  - Must be executed using `python3 -m doctest -v tests/101-lazy_matrix_mul.txt`.

### Task 8: CPython #3: Python Strings

- **File:** `102-python.c`
- **Description:**
  - Implements a CPython extension function (`print_python_string`) to print Python strings.
  - Validates and prints information about the given string object.
  - Requires compilation using `gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c`.
  - Includes a test script (`102-tests.py`) for demonstration.
