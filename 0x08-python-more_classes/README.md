### Tasks

#### 0. Simple rectangle
- Write an empty class `Rectangle` that defines a rectangle.
- You are not allowed to import any module.
- Example usage:
  ```python
  Rectangle = __import__('0-rectangle').Rectangle

  my_rectangle = Rectangle()
  print(type(my_rectangle))
  print(my_rectangle.__dict__)
  ```

#### 1. Real definition of a rectangle
- Write a class `Rectangle` that defines a rectangle with the following specifications:
  - Private instance attribute: `width`.
    - Property method `def width(self):` to retrieve it.
    - Property setter method `def width(self, value):` to set it.
      - Width must be an integer, otherwise raise a `TypeError` exception with the message "width must be an integer."
      - If width is less than 0, raise a `ValueError` exception with the message "width must be >= 0."
  - Private instance attribute: `height`.
    - Property method `def height(self):` to retrieve it.
    - Property setter method `def height(self, value):` to set it.
      - Height must be an integer, otherwise raise a `TypeError` exception with the message "height must be an integer."
      - If height is less than 0, raise a `ValueError` exception with the message "height must be >= 0."
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Example usage:
    ```python
    Rectangle = __import__('1-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
    ```

#### 2. Area and Perimeter
- Write a class `Rectangle` that defines a rectangle with the following specifications (based on Task 1):
  - Public instance method `def area(self):` that returns the rectangle area.
  - Public instance method `def perimeter(self):` that returns the rectangle perimeter:
    - If width or height is equal to 0, perimeter is equal to 0.
  - Example usage:
    ```python
    Rectangle = __import__('2-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    my_rectangle.width = 10
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
    ```

#### 3. String representation
- Write a class `Rectangle` that defines a rectangle with the following specifications (based on Task 2):
  - Public instance method `def area(self):` that returns the rectangle area.
  - Public instance method `def perimeter(self):` that returns the rectangle perimeter:
    - If width or height is equal to 0, perimeter has to be equal to 0.
  - `print()` and `str()` should print the rectangle with the character `#`.
    - If width or height is equal to 0, return an empty string.
  - Example usage:
    ```python
    Rectangle = __import__('3-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
    print(str(my_rectangle))
    print(repr(my_rectangle))

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle)
    print(repr(my_rectangle))
    ```

#### 4. Eval is magic
- Write a class `Rectangle` that defines a rectangle with the following specifications (based on Task 3):
  - `print()` and `str()` should print the rectangle with the character `#`.
    - If width or height is equal to 0, return an empty string.
  - `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.
  - Example usage:
    ```python
    Rectangle = __import__('4-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # create a new instance based on representation
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))
    ```

#### 5. Detect instance deletion
- Write a class `Rectangle` that defines a rectangle with the following specifications (based on Task 4):
  - Print the message "Bye rectangle..." when an instance of Rectangle is deleted.
  - Example usage:
    ```python
    Rectangle = __import__('5-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    del my_rectangle

    try:
        print(my_rectangle)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    ```

#### 6. How many instances
- Write a class `Rectangle` that defines a rectangle with the following specifications (based on Task 5):
  - Public class attribute `number_of_instances`:
    - Initialized to 0.
    - Incremented during each new instance instantiation.
    - Decremented during each instance deletion.
  - Example usage:
    ```python
    Rectangle = __import__('6-rectangle').Rectangle

    my_rectangle_1 = Rectangle(2, 4)
    my_rectangle_2 = Rectangle(2, 4)
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
    del my_rectangle_1
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
    del my_rectangle_2
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
    ```

#### 7. Change representation
- Write a class `Rectangle` that defines a rectangle with the following specifications (based on Task 6):
  - Public class attribute `print_symbol`:
    - Initialized to `#`.
    - Used as a symbol for string representation.
    - Can be any type.
  - Example usage:
    ```python
    Rectangle = __import__('7-rectangle').Rectangle

    my_rectangle_1 = Rectangle(8, 4)
    print(my_rectangle_1)
    print("--")
    my_rectangle_1.print_symbol = "&"
    print(my_rectangle_1)
    print("--")

    my_rectangle_2 = Rectangle(2, 1)
    print(my_rectangle_2)
    print("--")
    Rectangle.print_symbol = "C"
    print(my_rectangle_2)
    print("--")

    my_rectangle_3 = Rectangle(7, 3)
    print(my_rectangle_3)

    print("--")

    my_rectangle_

3.print_symbol = ["C", "is", "fun!"]
    print(my_rectangle_3)
    ```

#### 8. Compare rectangles
- Write a class `Rectangle` that defines a rectangle with the following specifications (based on Task 7):
  - Public class attribute `print_symbol`:
    - Initialized to `#`.
    - Used as a symbol for string representation.
    - Can be any type.
  - Public class attribute `class_symbol`:
    - Initialized to `Rectangle`.
    - Used as a symbol for string representation of the class.
    - Can be any type.
  - Public instance method `def bigger_or_equal(self, rect_1, rect_2):` that returns the biggest rectangle based on the area.
    - If both have the same area value, return rect_1.
    - If `rect_1` is not an instance of `Rectangle`, raise a `TypeError` with the message "rect_1 must be an instance of Rectangle".
    - If `rect_2` is not an instance of `Rectangle`, raise a `TypeError` with the message "rect_2 must be an instance of Rectangle".
  - Example usage:
    ```python
    Rectangle = __import__('8-rectangle').Rectangle

    my_rectangle_1 = Rectangle(8, 4)
    my_rectangle_2 = Rectangle(2, 3)

    if my_rectangle_1.bigger_or_equal(my_rectangle_1, my_rectangle_2) is my_rectangle_1:
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")

    my_rectangle_2.width = 10
    my_rectangle_2.height = 5
    if my_rectangle_1.bigger_or_equal(my_rectangle_1, my_rectangle_2) is my_rectangle_2:
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    ```

#### 9. A square is a rectangle
- Write a class `Rectangle` that defines a rectangle with the following specifications (based on Task 8):
  - Public class attribute `print_symbol`:
    - Initialized to `#`.
    - Used as a symbol for string representation.
    - Can be any type.
  - Public class attribute `class_symbol`:
    - Initialized to `Rectangle`.
    - Used as a symbol for string representation of the class.
    - Can be any type.
  - Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
  - Public instance method `def area(self):` that returns the rectangle area.
  - Public instance method `def perimeter(self):` that returns the rectangle perimeter:
    - If width or height is equal to 0, perimeter is equal to 0.
  - `print()` and `str()` should print the rectangle with the character `#`.
    - If width or height is equal to 0, return an empty string.
  - Public instance method `def bigger_or_equal(self, rect_1, rect_2):` that returns the biggest rectangle based on the area.
    - If both have the same area value, return `rect_1`.
    - If `rect_1` is not an instance of `Rectangle`, raise a `TypeError` with the message "rect_1 must be an instance of Rectangle".
    - If `rect_2` is not an instance of `Rectangle`, raise a `TypeError` with the message "rect_2 must be an instance of Rectangle".
  - Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`.
  - Example usage:
    ```python
    Rectangle = __import__('9-rectangle').Rectangle

    my_square = Rectangle.square(5)
    print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
    print(my_square)

    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
    print(my_rectangle)
    ```

#### 10. N queens
- Write a class `NQueens` that solves the N-queens puzzle with the following specifications:
  - Class method `def solveNQueens(N):` that returns a list of all possible solutions to the N-queens puzzle.
  - Each solution is represented as a list of strings where each string represents a row in the board.
  - In each string, 'Q' represents a queen and '.' represents an empty space.
  - Solutions are represented in lexicographical order.
  - Example usage:
    ```python
    NQueens = __import__('101-nqueens').NQueens

    solutions = NQueens.solveNQueens(4)
    for solution in solutions:
        print(solution)
    ```
