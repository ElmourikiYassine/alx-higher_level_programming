Certainly! Below is the README file for the given tasks:

---

# Python Object-Relational Mapping (ORM) - Project

This project focuses on utilizing Python's SQLAlchemy library to perform Object-Relational Mapping for a MySQL database. The tasks involve creating, querying, and manipulating data in the database using Python scripts.

## Prerequisites

- Python 3.x
- MySQL server
- MySQLdb module
- SQLAlchemy module

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/alx-higher_level_programming.git
   ```

2. Navigate to the project directory:

   ```bash
   cd alx-higher_level_programming/0x0F-python-object_relational_mapping
   ```

## Task Descriptions

### Task 0: Get all states

Write a script (`0-select_states.py`) that lists all states from the database `hbtn_0e_0_usa`. The script takes three arguments: MySQL username, MySQL password, and database name.

```bash
./0-select_states.py root root hbtn_0e_0_usa
```

### Task 1: Filter states

Write a script (`1-filter_states.py`) that lists all states with a name starting with 'N' from the database `hbtn_0e_0_usa`.

```bash
./1-filter_states.py root root hbtn_0e_0_usa
```

### Task 2: Filter states by user input

Write a script (`2-my_filter_states.py`) that takes a state name as an argument and displays all values in the states table where the name matches the argument.

```bash
./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
```

### Task 3: SQL Injection...

Write a script (`3-my_safe_filter_states.py`) similar to Task 2 but safe from SQL injection.

```bash
./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
```

### Task 4: Cities by states

Write a script (`4-cities_by_state.py`) that lists all cities from the database `hbtn_0e_4_usa`.

```bash
./4-cities_by_state.py root root hbtn_0e_4_usa
```

### Task 5: All cities by state

Write a script (`5-filter_cities.py`) that takes a state name as an argument and lists all cities of that state from the database `hbtn_0e_4_usa`.

```bash
./5-filter_cities.py root root hbtn_0e_4_usa Texas
```

### Task 6: First state model

Write a Python file (`model_state.py`) containing the class definition of a State and an instance `Base = declarative_base()`.

```bash
cat 6-model_state.sql | mysql -uroot -p
./6-model_state.py root root hbtn_0e_6_usa
```

### Task 7: All states via SQLAlchemy

Write a script (`7-model_state_fetch_all.py`) that lists all State objects from the database `hbtn_0e_6_usa`.

```bash
cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
./7-model_state_fetch_all.py root root hbtn_0e_6_usa
```

### Task 8: First state

Write a script (`8-model_state_fetch_first.py`) that prints the first State object from the database `hbtn_0e_6_usa`.

```bash
./8-model_state_fetch_first.py root root hbtn_0e_6_usa
```

### Task 9: Contains `a`

Write a script (`9-model_state_filter_a.py`) that lists all State objects containing the letter 'a' from the database `hbtn_0e_6_usa`.

```bash
./9-model_state_filter_a.py root root hbtn_0e_6_usa
```

### Task 10: Get a state

Write a script (`10-model_state_my_get.py`) that prints the State object's id with the given name from the database `hbtn_0e_6_usa`.

```bash
./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
```

### Task 11: Add a new state

Write a script (`11-model_state_insert.py`) that adds the State object "Louisiana" to the database `hbtn_0e_6_usa`.

```bash
./11-model_state_insert.py root root hbtn_0e_6_usa
```

### Task 12: Update a state

Write a script (`12-model_state_update_id_2.py`) that changes the name of a State object with id=2 to "New Mexico" in the database `hbtn_0e_6_usa`.

```bash
./12-model_state_update_id_2.py root root hbtn_0e_

6_usa
```

### Task 13: Delete states

Write a script (`13-model_state_delete_a.py`) that deletes all State objects containing the letter 'a' from the database `hbtn_0e_6_usa`.

```bash
./13-model_state_delete_a.py root root hbtn_0e_6_usa
```
