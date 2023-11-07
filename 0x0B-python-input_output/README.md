# README for alx-higher_level_programming

## Table of Contents
1. [Read File](#read-file)
2. [Write to a File](#write-to-a-file)
3. [Append to a File](#append-to-a-file)
4. [To JSON String](#to-json-string)
5. [From JSON String to Object](#from-json-string-to-object)
6. [Save Object to a File](#save-object-to-a-file)
7. [Create Object from a JSON File](#create-object-from-a-json-file)
8. [Load, Add, Save](#load-add-save)
9. [Class to JSON](#class-to-json)
10. [Student to JSON](#student-to-json)
11. [Student to JSON with Filter](#student-to-json-with-filter)
12. [Student to Disk and Reload](#student-to-disk-and-reload)
13. [Pascal's Triangle](#pascals-triangle)

---

## 1. Read File
### File: 0x0B-python-input_output/0-read_file.py
- Prototype: `def read_file(filename=""):`
- Function reads a text file (UTF8) and prints it to stdout.
- Usage example:
  ```python
  read_file = __import__('0-read_file').read_file
  read_file("my_file_0.txt")
  ```

---

## 2. Write to a File
### File: 0x0B-python-input_output/1-write_file.py
- Prototype: `def write_file(filename="", text=""):`
- Function writes a string to a text file (UTF8) and returns the number of characters written.
- Usage example:
  ```python
  write_file = __import__('1-write_file').write_file
  nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
  print(nb_characters)
  ```

---

## 3. Append to a File
### File: 0x0B-python-input_output/2-append_write.py
- Prototype: `def append_write(filename="", text=""):`
- Function appends a string at the end of a text file (UTF8) and returns the number of characters added.
- Usage example:
  ```python
  append_write = __import__('2-append_write').append_write
  nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
  print(nb_characters_added)
  ```

---

## 4. To JSON String
### File: 0x0B-python-input_output/3-to_json_string.py
- Prototype: `def to_json_string(my_obj):`
- Function returns the JSON representation of an object (string).
- Usage example:
  ```python
  to_json_string = __import__('3-to_json_string').to_json_string
  my_list = [1, 2, 3]
  s_my_list = to_json_string(my_list)
  print(s_my_list)
  ```

---

## 5. From JSON String to Object
### File: 0x0B-python-input_output/4-from_json_string.py
- Prototype: `def from_json_string(my_str):`
- Function returns an object (Python data structure) represented by a JSON string.
- Usage example:
  ```python
  from_json_string = __import__('4-from_json_string').from_json_string
  s_my_list = "[1, 2, 3]"
  my_list = from_json_string(s_my_list)
  print(my_list)
  ```

---

## 6. Save Object to a File
### File: 0x0B-python-input_output/5-save_to_json_file.py
- Prototype: `def save_to_json_file(my_obj, filename):`
- Function writes an Object to a text file, using a JSON representation.
- Usage example:
  ```python
  save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
  filename = "my_list.json"
  my_list = [1, 2, 3]
  save_to_json_file(my_list, filename)
  ```

---

## 7. Create Object from a JSON File
### File: 0x0B-python-input_output/6-load_from_json_file.py
- Prototype: `def load_from_json_file(filename):`
- Function creates an Object from a “JSON file”.
- Usage example:
  ```python
  load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
  filename = "my_list.json"
  my_list = load_from_json_file(filename)
  print(my_list)
  ```

---

## 8. Load, Add, Save
### File: 0x0B-python-input_output/7-add_item.py
- Script that adds all arguments to a Python list and then saves them to a file using JSON representation.
- Usage example:
  ```bash
  ./7-add_item.py Best School
  ```

---

## 9. Class to JSON
### File: 0x0B-python-input_output/8-class_to_json.py
- Prototype: `def class_to_json(obj):`
- Function returns the dictionary description with a simple data structure for JSON serialization of an object.
- Usage example:
  ```python
  MyClass = __import__('8-my_class').MyClass
  class_to_json = __import__('8-class_to_json').class_to_json
  m = MyClass("John")
  mj = class_to_json(m)
  print(mj)
  ```

---

## 10. Student to JSON
### File: 0x0B-python-input_output/9-student.py
- Class `Student` that defines a student with public instance attributes.
- Method `to_json` retrieves a dictionary representation of a `Student` instance.
- Usage example:
  ```python
  Student = __import__('9-student').Student
  students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]
  for student in students:
      j_student = student.to_json()
      print(j_student)
  ```

---

## 11. Student to JSON with Filter
### File: 0x0B-python-input_output/10-student.py
- Class `Student` with method `to_json` that retrieves a dictionary representation based on a list of attributes.
- Usage example:
  ```python
  Student = __import__('10-student').Student
  student_1 = Student("John", "Doe", 23)
  j_student_1 = student_1.to_json()
  print(j_student_1)
  j_student_2 = student_1.to_json(['first_name', 'age'])
  print(j_student_2)
  ```

---
