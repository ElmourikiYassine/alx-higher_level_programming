---

# SQL Practice Readme

This repository contains a set of SQL scripts designed to practice various aspects of SQL, including user management, table creation, and data querying.

## Scripts:

### 0-privileges.sql
- Display privileges for two users: 'user_0d_1' and 'user_0d_2'.

### 1-create_user.sql
- Create 'user_0d_1' with full privileges.

### 2-create_read_user.sql
- Create 'user_0d_2' with SELECT privilege on a specific database.

### 3-force_name.sql
- Create a table named 'force_name' with an enforced NOT NULL constraint on the 'name' column.

### 4-never_empty.sql
- Create a table named 'id_not_null' with a default value for 'id' and no NULL values for 'name'.

### 5-unique_id.sql
- Create a table named 'unique_id' with a UNIQUE constraint on the 'id' column.

### 6-states.sql
- Create a database 'hbtn_0d_usa' with a 'states' table having an AUTO_INCREMENT primary key.

### 7-cities.sql
- Create a 'cities' table with a FOREIGN KEY reference to the 'states' table.

### 8-cities_of_california_subquery.sql
- Select cities of California without using JOIN.

### 9-cities_by_state_join.sql
- Select all cities with their corresponding state names using JOIN.

### 10-genre_id_by_show.sql
- Select shows with at least one genre linked.

### 11-genre_id_all_shows.sql
- Select all shows with their genre IDs.

### 12-no_genre.sql
- Select shows without a genre linked.

### 13-count_shows_by_genre.sql
- Count shows by genre.

### 14-my_genres.sql
- List genres of the show 'Dexter'.

### 15-comedy_only.sql
- List Comedy shows.

### 16-shows_by_genre.sql
- List shows and their genres.

### 17-not_my_genres.sql
- List genres not linked to the show 'Dexter'.

### 101-not_a_comedy.sql
- List shows without the genre 'Comedy'.

### 102-rating_shows.sql
- List shows by their rating.

### 103-best_genre.sql
- List genres by their total rating sum.

---
