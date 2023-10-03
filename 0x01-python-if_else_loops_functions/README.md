---

## Task 0: Positive or Negative
**Repo:**
- GitHub Repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- File: 0-positive_or_negative.py

**Instructions:**
- This program will assign a random signed number to the variable `number` each time it is executed.
- Complete the source code to print whether the number stored in the variable `number` is positive or negative.
- Do not modify the existing code related to `import` and `random.randint`.

**Output:**
```bash
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-4 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-3 is negative
...
```

---

## Task 1: The Last Digit
**Repo:**
- GitHub Repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- File: 1-last_digit.py

**Instructions:**
- This program will assign a random signed number to the variable `number` each time it is executed.
- Complete the source code to print the last digit of the number stored in the variable `number`.

**Output:**
```bash
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
...
```

---

## Task 2: Print Alphabet
**Repo:**
- GitHub Repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- File: 2-print_alphabet.py

**Instructions:**
- Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
- Use only one `print` function with string format.
- Use only one loop in your code.
- Do not store characters in a variable.
- Do not import any module.

**Output:**
```bash
guillaume@ubuntu:~/0x01$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyz
guillaume@ubuntu:~/0x01$
```
---

## Task 3: Exclude 'q' and 'e' from Alphabet
**Repo:**
- GitHub Repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- File: 3-print_alphabt.py

**Instructions:**
- Write a program that prints the ASCII alphabet, in lowercase, excluding the letters 'q' and 'e'.
- Use only one `print` function with string format.
- Use only one loop in your code.
- Do not store characters in a variable.
- Do not import any module.

**Output:**
```bash
guillaume@ubuntu:~/0x01$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyz
guillaume@ubuntu:~/0x01$
```

---

## Task 4: Hexadecimal Printing
**Repo:**
- GitHub Repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- File: 4-print_hexa.py

**Instructions:**
- Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal.
- Use only one `print` function with string format.
- Use only one loop in your code.
- Do not store numbers or strings in a variable.
- Do not import any module.

**Output:**
```bash
guillaume@ubuntu:~/0x01$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
...
96 = 0x60
97 = 0x61
98 = 0x62
guillaume@ubuntu:~/0x01$
```
---

## Task 5: Print 00...99
**Repo:**
- GitHub Repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- File: 5-print_comb2.py

**Instructions:**
- Write a program that prints numbers from 0 to 99.
- Numbers must be separated by `, `, followed by a space.
- Numbers should be printed in ascending order, with two digits.
- The last number should be followed by a new line.
- Use no more than 2 `print` functions with string format.
- Use only one loop in your code.
- Do not store numbers or strings in a variable.
- Do not import any module.

**Output:**
```bash
guillaume@ubuntu:~/0x01$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
guillaume@ubuntu:~/0x01$
```

---

## Task 6: Print Combinations of Two Digits
**Repo:**
- GitHub Repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- File: 6-print_comb3.py

**Instructions:**
- Write a program that prints all possible different combinations of two digits.
- Numbers must be separated by `, `, followed by a space.
- The two digits must be different.
- `01` and `10` are considered the same combination of the two digits `0` and `1`.
- Print only the smallest combination of two digits.
- Numbers should be printed in ascending order, with two digits.
- The last number should be followed by a new line.
- Use no more than 3 `print` functions with string format.
- Use no more than 2 loops in your code.
- Do not store numbers or strings in a variable.
- Do not import any module.

**Output:**
```bash
guillaume@ubuntu:~/0x01$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
guillaume@ubuntu:~/0x01$
```
Certainly! Continuing with the Markdown representation for the remaining tasks:

---

## Task 7: Check for Lowercase Character
**Repo:**
- GitHub Repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- File: 7-islower.py

**Instructions:**
- Write a function that checks for a lowercase character.
- Prototype: `def islower(c):`
- Returns True if `c` is lowercase, False otherwise.
- Do not import any module.
- Do not use `str.upper()` and `str.isupper()`.
- Tips: `ord()`
- You don’t need to understand `__import__`.

**Example:**
```python
guillaume@ubuntu:~/0x01$ cat 7-main.py
#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

guillaume@ubuntu:~/0x01$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
guillaume@ubuntu:~/0x01$
```

---

## Task 8: Convert to Uppercase
**Repo:**
- GitHub Repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- File: 8-uppercase.py

**Instructions:**
- Write a function that prints a string in uppercase followed by a new line.
- Prototype: `def uppercase(str):`
- Use no more than 2 `print` functions with string format.
- Use only one loop in your code.
- Do not import any module.
- Do not use `str.upper()` and `str.isupper()`.
- Tips: `ord()`
- You don’t need to understand `__import__`.

**Example:**
```python
guillaume@ubuntu:~/0x01$ cat 8-main.py
#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")

guillaume@ubuntu:~/0x01$ ./8-main.py
BEST
BEST SCHOOL 98 BATTERY STREET
guillaume@ubuntu:~/0x01$
```
Absolutely! Let's continue with the Markdown representation for the remaining tasks:

---

## Task 9: Print Last Digit
**Repo:**
- GitHub Repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- File: 9-print_last_digit.py

**Instructions:**
- Write a function that prints the last digit of a number.
- Prototype: `def print_last_digit(number):`
- Returns the value of the last digit.
- Do not import any module.
- You don’t need to understand `__import__`.

**Example:**
```python
guillaume@ubuntu:~/0x01$ cat 9-main.py
#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

guillaume@ubuntu:~/0x01$ ./9-main.py
8044
guillaume@ubuntu:~/0x01$
```

---

## Task 10: Add Two Integers
**Repo:**
- GitHub Repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- File: 10-add.py

**Instructions:**
- Write a function that adds two integers and returns the result.
- Prototype: `def add(a, b):`
- Returns the value of `a + b`.
- Do not import any module.
- You don’t need to understand `__import__`.

**Example:**
```python
guillaume@ubuntu:~/0x01$ cat 10-main.py
#!/usr/bin/env python3
add = __import__('10-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))

guillaume@ubuntu:~/0x01$ ./10-main.py
3
98
98
guillaume@ubuntu:~/0x01$
```

---

## Task 11: Power Function
**Repo:**
- GitHub Repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- File: 11-pow.py

**Instructions:**
- Write a function that computes `a` to the power of `b` and returns the value.
- Prototype: `def pow(a, b):`
- Returns the value of `a ^ b`.
- Do not import any module.
- You don’t need to understand `__import__`.

**Example:**
```python
guillaume@ubuntu:~/0x01$ cat 11-main.py
#!/usr/bin/env python3
pow = __import__('11-pow').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

guillaume@ubuntu:~/0x01$ ./11-main.py
4
9604
1
0.0001
-1024
guillaume@ubuntu:~/0x01$
```
Certainly! Let's continue with the Markdown representation for the remaining tasks:

---

## Task 12: Fizz Buzz
**Repo:**
- GitHub Repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- File: 12-fizzbuzz.py

**Instructions:**
- Write a function that prints the numbers from 1 to 100 separated by a space.
- For multiples of three, print "Fizz" instead of the number.
- For multiples of five, print "Buzz" instead of the number.
- For numbers which are multiples of both three and five, print "FizzBuzz".
- Prototype: `def fizzbuzz():`
- Each element should be followed by a space.
- Do not import any module.
- You don’t need to understand `__import__`.

**Example:**
```python
guillaume@ubuntu:~/0x01$ cat 12-main.py
#!/usr/bin/env python3
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")

guillaume@ubuntu:~/0x01$ ./12-main.py | cat -e
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
guillaume@ubuntu:~/0x01$
```

---

## Task 13: Insert in Sorted Linked List
**Repo:**
- GitHub Repository: alx-higher_level_programming
- Directory: 0x01-python-if_else_loops_functions
- Files: 13-insert_number.c, lists.h

**Instructions:**
- Write a C function that inserts a number into a sorted singly linked list.
- Prototype: `listint_t *insert_node(listint_t **head, int number);`
- Return: the address of the new node, or NULL if it failed.
- You are not allowed to google anything.
- Whiteboard first.

**Example:**
```c
carrie@ubuntu:0x01$ cat lists.h 
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
carrie@ubuntu:0x01$ cat linked_lists.c 
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
carrie@ubuntu:0x01$ cat 13-main.c 
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head =

 NULL;
    add_nodeint_end(&head, 0);
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 3);
    add_nodeint_end(&head, 4);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 402);
    add_nodeint_end(&head, 1024);

    printf("Original list:\n");
    print_listint(head);

    insert_node(&head, 27);

    printf("Inserted 27:\n");
    print_listint(head);

    insert_node(&head, -3);

    printf("Inserted -3:\n");
    print_listint(head);

    insert_node(&head, 1034);

    printf("Inserted 1034:\n");
    print_listint(head);

    free_listint(head);

    return (0);
}
carrie@ubuntu:0x01$ gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-insert_number.c -o insert
carrie@ubuntu:0x01$ ./insert
Original list:
0
1
2
3
4
98
402
1024
Inserted 27:
0
1
2
3
4
27
98
402
1024
Inserted -3:
-3
0
1
2
3
4
27
98
402
1024
Inserted 1034:
-3
0
1
2
3
4
27
98
402
1024
1034
```
---
