# SQL Introduction

This repository contains SQL scripts for various tasks related to database management using MySQL.

## Tasks Overview:

### 0. List Databases

Script: [0-list_databases.sql](0-list_databases.sql)

Lists all databases on the MySQL server.

### 1. Create a Database if Missing

Script: [1-create_database_if_missing.sql](1-create_database_if_missing.sql)

Creates the database `hbtn_0c_0` if it doesn't already exist.

### 2. Delete a Database

Script: [2-remove_database.sql](2-remove_database.sql)

Deletes the database `hbtn_0c_0` if it exists.

### 3. List Tables

Script: [3-list_tables.sql](3-list_tables.sql)

Lists all tables in the `hbtn_0c_0` database.

### 4. First Table

Script: [4-first_table.sql](4-first_table.sql)

Creates a table named `first_table` in the `hbtn_0c_0` database.

### 5. Full Description

Script: [5-full_table.sql](5-full_table.sql)

Prints the full description of the `first_table` in the `hbtn_0c_0` database.

### 6. List All in Table

Script: [6-list_values.sql](6-list_values.sql)

Lists all rows in the `first_table` in the `hbtn_0c_0` database.

### 7. First Add

Script: [7-insert_value.sql](7-insert_value.sql)

Inserts a new row with id=89 and name='Best School' into `first_table`.

### 8. Count 89

Script: [8-count_89.sql](8-count_89.sql)

Counts the number of records with id=89 in `first_table`.

### 9. Full Creation

Script: [9-full_creation.sql](9-full_creation.sql)

Creates a table named `second_table` and inserts multiple rows into it.

### 10. List by Best

Script: [10-top_score.sql](10-top_score.sql)

Lists all records in `second_table` ordered by score in descending order.

### 11. Select the Best

Script: [11-best_score.sql](11-best_score.sql)

Lists records with a score >= 10 in `second_table` ordered by score.

### 12. Cheating is Bad

Script: [12-no_cheating.sql](12-no_cheating.sql)

Updates the score of 'Bob' to 10 in `second_table` without using Bob's id.

### 13. Score Too Low

Script: [13-change_class.sql](13-change_class.sql)

Removes records with a score <= 5 in `second_table`.

### 14. Average

Script: [14-average.sql](14-average.sql)

Computes the average score of all records in `second_table`.

### 15. Number by Score

Script: [15-groups.sql](15-groups.sql)

Lists the number of records for each score in `second_table`, ordered by the number of records.

### 16. Say My Name

Script: [16-no_link.sql](16-no_link.sql)

Lists all records in `second_table` with a name, ordered by score in descending order.

### 17. Go to UTF8

Script: [100-move_to_utf8.sql](100-move_to_utf8.sql)

Converts the `hbtn_0c_0` database, `first_table` table, and `name` field to UTF8.

---
