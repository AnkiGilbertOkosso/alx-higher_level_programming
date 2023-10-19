
# 0x0D. SQL - Introduction

**Author:** Anki Gilbert Okosso
**Date:** October 17, 2023

Welcome to my SQL Introduction project repository! This project focuses on various SQL concepts and tasks using MySQL on an Ubuntu 20.04 LTS server. Here, I will guide you through the tasks I completed for this project.

## Table of Contents
1. [Project Description](#project-description)
2. [Requirements](#requirements)
3. [Tasks](#tasks)
   - [List Databases](#task-0-list-databases)
   - [Create a Database](#task-1-create-a-database)
   - [Delete a Database](#task-2-delete-a-database)
   - [List Tables](#task-3-list-tables)
   - [Create a Table](#task-4-create-a-table)
   - [Full Table Description](#task-5-full-table-description)
   - [List All Records in a Table](#task-6-list-all-records-in-a-table)
   - [Insert a New Record](#task-7-insert-a-new-record)
   - [Count Records](#task-8-count-records)
   - [Full Table Creation](#task-9-full-table-creation)
   - [List by Best](#task-10-list-by-best)
   - [Select the Best](#task-11-select-the-best)
   - [Update a Record](#task-12-update-a-record)
   - [Delete Records](#task-13-delete-records)
   - [Calculate Average](#task-14-calculate-average)
   - [Number by Score](#task-15-number-by-score)
   - [Filter Records](#task-16-filter-records)
   - [Database Character Set](#task-17-database-character-set)
   - [Average Temperature](#task-18-average-temperature)
   - [Top Temperature](#task-19-top-temperature)
   - [Max Temperature by State](#task-20-max-temperature-by-state)

## Project Description

In this project, I explored the fundamentals of SQL, database management, and executed various SQL queries using MySQL. The project focuses on creating, modifying, and querying databases and tables, as well as performing data manipulation tasks.

## Requirements

- **Allowed Editors:** vi, vim, emacs
- **Operating System:** Ubuntu 20.04 LTS
- **MySQL Version:** 8.0 (8.0.25)
- **SQL Commands:** Uppercase (e.g., SELECT, WHERE)
- **Files:** All files should end with a new line
- **Comments:** All SQL queries should have a comment just before the query
- **README:** A `README.md` file is mandatory for this project
- **MySQL Installation:** Instructions provided for installing MySQL in Ubuntu 20.04

## Tasks

### Task 0: List Databases

I created a script to list all the databases on the MySQL server. Here's how to run it:

```shell
mysql -hlocalhost -uroot -p < 0-list_databases.sql
```

### Task 1: Create a Database

I created a script that creates the database `hbtn_0c_0` if it doesn't already exist. To run it:

```shell
mysql -hlocalhost -uroot -p < 1-create_database_if_missing.sql
```

### Task 2: Delete a Database

I created a script to delete the `hbtn_0c_0` database if it exists. To run the script:

```shell
mysql -hlocalhost -uroot -p < 2-remove_database.sql
```

### Task 3: List Tables

I wrote a script to list all the tables in a specific database. To run the following command:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 3-list_tables.sql
```

### Task 4: Create a Table

I created a table called `first_table` in the `hbtn_0c_0` database. Here's how to run the script:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 4-first_table.sql
```

### Task 5: Full Table Description

I wrote a script to display the full description of the `first_table`. To execute it, use:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 5-full_table.sql
```

### Task 6: List All Records in a Table

I created a script to list all rows in the `first_table`. Run it with this command:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 6-list_values.sql
```

### Task 7: Insert a New Record

I inserted a new row into `first_table`. Use the following command to run the script:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 7-insert_value.sql
```

### Task 8: Count Records

I wrote a script to count the number of records with `id = 89` in `

first_table`. To execute it, use this command:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 8-count_89.sql
```

### Task 9: Full Table Creation

I created the `second_table` and inserted multiple rows into it. Run the following command to execute the script:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 9-full_creation.sql
```

### Task 10: List by Best

I wrote a script to list all records from `second_table`, ordered by score (top first). To run it:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 10-top_score.sql
```

### Task 11: Select the Best

I created a script to list records with a score greater than or equal to 10 in `second_table`, ordered by score (top first). To execute it:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 11-best_score.sql
```

### Task 12: Update a Record

I wrote a script to update the score of a record with the name "Bob" to 10 in `second_table`. To run it:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 12-no_cheating.sql
```

### Task 13: Delete Records

I created a script to delete records with a score less than or equal to 5 in `second_table`. To execute it:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 13-change_class.sql
```

### Task 14: Calculate Average

I wrote a script that computes the average score of all records in `second_table`. Run the following command to execute the script:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 14-average.sql
```

### Task 15: Number by Score

I created a script that lists the number of records with the same score in `second_table`. The result includes the score and the number of records, ordered by the number of records (descending). To execute it:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 15-groups.sql
```

### Task 16: Filter Records

I wrote a script to list all records of `second_table`, excluding rows without a name value. The results display the score and the name (in this order) and are ordered by descending score. To run it:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 16-no_link.sql
```

### Task 17: Database Character Set

I created a script to convert the `hbtn_0c_0` database, the `first_table`, and the `name` field in `first_table` to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`). Use the following command to run the script:

```shell
mysql -hlocalhost -uroot -p < 100-move_to_utf8.sql
```

### Task 18: Average Temperature

I imported a table dump into the `hbtn_0c_0` database and wrote a script that displays the average temperature (in Fahrenheit) by city, ordered by temperature (descending). To run the script:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 101-avg_temperatures.sql
```

### Task 19: Top Temperature

I imported a table dump into the `hbtn_0c_0` database and created a script that displays the top 3 cities with the highest temperatures during July and August, ordered by temperature (descending). To run the script:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 102-top_city.sql
```

### Task 20: Max Temperature by State

I imported a table dump into the `hbtn_0c_0` database and created a script that displays the maximum temperature for each state, ordered by state name. To execute the script:

```shell
mysql -hlocalhost -uroot -p hbtn_0c_0 < 103-max_state.sql
```

