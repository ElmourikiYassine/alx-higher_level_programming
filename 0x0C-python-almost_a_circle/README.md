# alx-higher_level_programming

## 0x0C-python-almost_a_circle

This repository contains Python programs and classes that demonstrate various concepts related to object-oriented programming, unit testing, and file I/O. Each task is designed to build upon the previous one, forming a cohesive project that covers a range of topics.

### Tasks

#### Task 0: If it's not tested, it doesn't work

All files, classes, and methods must be unit tested and PEP 8 validated.

Example:
```bash
$ python3 -m unittest discover tests
...............
----------------------------------------------------------------------
Ran 15 tests in 0.001s

OK
```

#### Task 1: Base class

Write the first class `Base`:

- Create a folder named `models` with an empty file `__init__.py` inside, making it a Python package.
- Create a file named `models/base.py` with a class `Base`.
- The class should have a private class attribute `__nb_objects` initialized to 0.
- The class should have a class constructor `__init__(self, id=None)`:
  - If `id` is not `None`, assign it to the public instance attribute `id`.
  - Otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`.

Example:
```python
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)  # Output: 1

    b2 = Base()
    print(b2.id)  # Output: 2

    b3 = Base()
    print(b3.id)  # Output: 3

    b4 = Base(12)
    print(b4.id)  # Output: 12

    b5 = Base()
    print(b5.id)  # Output: 4
```

Repo:
- [GitHub repository](https://github.com/Elmourikiyassine/alx-higher_level_programming)
- Directory: `0x0C-python-almost_a_circle`
- File: `models/base.py`, `models/__init__.py`

#### Task 2: First Rectangle

Write the class `Rectangle` that inherits from `Base`:

- Create a file named `models/rectangle.py` with a class `Rectangle` that inherits from `Base`.
- The class should have private instance attributes `__width`, `__height`, `__x`, and `__y` with corresponding public getter and setter methods.
- The class constructor should be `__init__(self, width, height, x=0, y=0, id=None)`.
- The constructor should call the constructor of the `Base` class with `id` and initialize the attributes with the provided values.

Example:
```python
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)  # Output: 1

    r2 = Rectangle(2, 10)
    print(r2.id)  # Output: 2

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)  # Output: 12
```

Repo:
- [GitHub repository](https://github.com/Elmourikiyassine/alx-higher_level_programming)
- Directory: `0x0C-python-almost_a_circle`
- File: `models/rectangle.py`

#### Task 3: Validate attributes

Update the `Rectangle` class by adding validation to all setter methods and instantiation (excluding `id`):

- If the input is not an integer, raise `TypeError` with the message: `<name of the attribute> must be an integer`.
- If `width` or `height` is less than or equal to 0, raise `ValueError` with the message: `<name of the attribute> must be > 0`.
- If `x` or `y` is less than 0, raise `ValueError` with the message: `<name of the attribute> must be >= 0`.

Example:
```python
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))  # Output: [TypeError] height must be an integer

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))  # Output: [ValueError] width must be > 0

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))  # Output: [TypeError] x must be an integer

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))  # Output: [ValueError] y must be >= 0
```

Repo:
- [GitHub repository](https://github.com/Elmourikiyassine/alx-higher_level_programming)
- Directory: `0x0C-python-almost_a_circle`
- File: `models/rectangle.py`

#### Task 4: Area first

Update the `Rectangle` class by adding the public method `def area(self)` that returns the area value of the `Rectangle` instance.

Example:
```python
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())  # Output: 6

    r2 = Rectangle(2, 10)
    print(r2.area())  # Output: 20

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())  # Output: 56
```

Repo:
- [GitHub repository](https://github.com/Elmourikiyassine/alx-higher_level_programming)
- Directory: `0x0C-python-almost_a_circle`
- File: `models/rectangle.py`

#### Task 5: Display #0

Update the `Rectangle` class by adding the public method `def display(self)` that prints in stdout the `Rectangle` instance with the character `#`, ignoring `x` and `y`.

Example:
```python
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()
    '''
    ####
    ####
    ####
    ####
    ####
    ####
    '''

    print("---")

    r2 = Rectangle(2, 2)
    r2.display()
    '''
    ##
    ##
    '''
```

Repo:
- [GitHub repository](https://github.com/Elmourikiyassine/alx-higher_level_programming)
- Directory: `0x0C-python-almost_a_circle`
- File: `models/rectangle.py`

#### Task 6: `__str__`

Update the `Rectangle` class by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width

>/<height>`.

Example:
```python
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1)
    print(r1)  # Output: [Rectangle] (1) 2/1 - 4/6

    r2 = Rectangle(5, 5, 1)
    print(r2)  # Output: [Rectangle] (2) 1/0 - 5/5
```

Repo:
- [GitHub repository](https://github.com/Elmourikiyassine/alx-higher_level_programming)
- Directory: `0x0C-python-almost_a_circle`
- File: `models/rectangle.py`

#### Task 7: Display #1

Update the `Rectangle` class by improving the `display` method:

- Add the public method `def display(self):` to the `Rectangle` class that prints in stdout the `Rectangle` instance with the character `#`.
- The `Rectangle` class should now use the `__str__` method for printing.

Example:
```python
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()
    '''
    [Rectangle] (1) 0/0 - 4/6
    ----
    ####
    ####
    ####
    ####
    ####
    ####
    '''

    print("---")

    r2 = Rectangle(2, 2)
    r2.display()
    '''
    [Rectangle] (2) 0/0 - 2/2
    --
    ##
    ##
    '''
```

Repo:
- [GitHub repository](https://github.com/Elmourikiyassine/alx-higher_level_programming)
- Directory: `0x0C-python-almost_a_circle`
- File: `models/rectangle.py`

#### Task 8: Update #0

Update the `Rectangle` class by adding the public method `def update(self, *args, **kwargs)` that assigns attributes:

- If `args` is not empty, assign each argument to the corresponding attribute (`id`, `width`, `height`, `x`, and `y`) in this order.
- If `args` is empty, assign the corresponding attribute to each key/value pair in `kwargs`.

Example:
```python
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)  # Output: [Rectangle] (1) 10/10 - 10/10

    r1.update(89)
    print(r1)  # Output: [Rectangle] (89) 10/10 - 10/10

    r1.update(89, 1)
    print(r1)  # Output: [Rectangle] (89) 10/10 - 1/10

    r1.update(89, 1, 2)
    print(r1)  # Output: [Rectangle] (89) 10/10 - 1/2

    r1.update(89, 1, 2, 3)
    print(r1)  # Output: [Rectangle] (89) 3/10 - 1/2

    r1.update(89, 1, 2, 3, 4)
    print(r1)  # Output: [Rectangle] (89) 3/4 - 1/2

    r1.update(89, 1, 2, 3, 4, 5)
    print(r1)  # Output: [Rectangle] (89) 3/4 - 1/2

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)  # Output: [Rectangle] (89) 1/3 - 4/2
```

Repo:
- [GitHub repository](https://github.com/Elmourikiyassine/alx-higher_level_programming)
- Directory: `0x0C-python-almost_a_circle`
- File: `models/rectangle.py`

#### Task 9: Update #1

Update the `Rectangle` class by updating the public method `def update(self, *args, **kwargs)`:

- Assign the attributes in this order: `id`, `width`, `height`, `x`, and `y`.
- If `kwargs` is not empty, assign the attributes to each key/value pair in `kwargs`.
- The `Rectangle` class should now use the `__str__` method for printing.

Example:
```python
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)  # Output: [Rectangle] (1) 10/10 - 10/10

    r1.update(89)
    print(r1)  # Output: [Rectangle] (89) 10/10 - 10/10

    r1.update(89, 1)
    print(r1)  # Output: [Rectangle] (89) 10/10 - 1/10

    r1.update(89, 1, 2)
    print(r1)  # Output: [Rectangle] (89) 10/10 - 1/2

    r1.update(89, 1, 2, 3)
    print(r1)  # Output: [Rectangle] (89) 3/10 - 1/2

    r1.update(89, 1, 2, 3, 4)
    print(r1)  # Output: [Rectangle] (89) 3/4 - 1/2

    r1.update(89, 1, 2, 3, 4, 5)
    print(r1)  # Output: [Rectangle] (89) 3/4 - 1/2

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)  # Output: [Rectangle] (89) 1/3 - 4/2
```

Repo:
- [GitHub repository](https://github.com/Elmourikiyassine/alx-higher_level_programming)
- Directory: `0x0C-python-almost_a_circle`
- File: `models/rectangle.py`

#### Task 10: And now, the Square!

Write the class `Square` that inherits from `Rectangle`:

- Create a file named `models/square.py` with a class `Square` that inherits from `Rectangle`.
- The class should have a private instance attribute `__size` with corresponding getter and setter methods.
- The class constructor should be `def __init__(self, size, x=0, y=0, id=None)`:
  - Call the constructor of the `Base` class with `id`.
  - Call the constructor of the `Rectangle` class with the rest of the arguments.
- Override the `__str__` method in the `Square` class to return `[Square] (<id>) <x>/<y> - <size>`.

Example:
```python
from models.square
