# Tasks

## Task 0: Run Python file

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable `$PYFILE`.

```bash
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$
```

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 0-run

## Task 1: Run inline

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable `$PYCODE`.

```bash
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$
```

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 1-run_inline

## Task 2: Hello, print

Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print.

```bash
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 2-print.py

## Task 3: Print integer

Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

You can find the source code [here](https://github.com/ElmourikiYassine/alx-higher_level_programming).

The output of the script should be:
the number, followed by Battery street,
followed by a new line
You are not allowed to cast the variable number into a string
Your code must be 3 lines long
You have to use f-strings tips

```bash
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$
```

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 3-print_number.py

## Task 4: Print float

Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

You can find the source code [here](https://github.com/ElmourikiYassine/alx-higher_level_programming).

The output of the program should be:
Float:, followed by the float with only 2 digits
followed by a new line
You are not allowed to cast number to string
You have to use f-strings

```bash
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$
```

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 4-print_float.py

## Task 5: Print string

Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

You can find the source code [here](https://github.com/ElmourikiYassine/alx-higher_level_programming).

The output of the program should be:
3 times the value of str
followed by a new line
followed by the 9 first characters of str
followed by a new line
You are not allowed to use any loops or conditional statement
Your program should be maximum 5 lines long

```bash
guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$
```

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 5-print_string.py

## Task 6: Play with strings

Complete this source code to print Welcome to Holberton School!

You can find the source code [here](https://github.com/ElmourikiYassine/alx-higher_level_programming).

You are not allowed to use any loops or conditional statements.
You have to use the variables str1 and str2 in your new line of code
Your program should be exactly 5 lines long

```bash
guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$
```

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 6-concat.py

## Task 7: Copy - Cut - Paste

Complete this source code

You can find the source code [here](https://github.com/ElmourikiYassine/alx-higher_level_programming).

You are not allowed to use any loops or conditional statements
Your program should be exactly 8 lines long
word_first_3 should contain the first 3 letters of the variable word
word_last_2 should contain the last 2 letters of the variable word
middle_word should contain the value of the variable word without the first and last letters

```bash
guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/0x00$
```

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 7-edges.py

## Task 8: Create a new sentence

Complete this source code to print object-oriented programming with Python, followed by a new line.

You can find the source code [here](https://github.com/ElmourikiYassine/alx-higher_level_programming).

You are not allowed to use any loops or conditional statements
Your program should be exactly 5 lines long
You are not allowed to create new variables
You are not allowed to use string literals

```bash
guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$
```

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 8-concat_edges.py

## Task 9: Easter Egg

Write a Python script that prints “The Zen of Python”, by Tim Peters, followed by a new line.


