# MySQL Project 

This MySQL project showcases my skills in managing a MySQL database, creating tables, and performing various database operations. The project covers a range of tasks related to MySQL and is intended to demonstrate my proficiency in database management.

## Prerequisites

Before running these scripts, ensure that you have the following:

1. MySQL Server Installed: Make sure you have MySQL Server (version 5.7) installed on your machine or a server where you plan to run these scripts.

2. MySQL Client: You should have the MySQL client installed to interact with the MySQL server.

## Tasks

### Task 0: List All Privileges

I wrote a script to list all privileges of the MySQL users. It retrieves this information from the `information_schema` database.

### Task 1: Create a New User

I created a new MySQL user with specific privileges on the database. The user name is "Holberton," and it has the SELECT privilege on all users in the database and the privilege to access all tables of all databases.

### Task 2: List All Databases

A script lists all databases on your MySQL server.

### Task 3: Insecure Password

I created a new user with an insecure password and specific privileges on tables and databases.

### Task 4: Secure Password

I created a new user with a secure password and the same privileges as in Task 3.

### Task 5: Create a Table

A script creates a table called "students" in the "tutorial_db" database. The table has specific columns and constraints.

### Task 6: No Table for a User

A script creates the "users" table only if it does not already exist in the "tutorial_db" database.

### Task 7: Drop to Be Alive

I wrote a script to delete the "users" table if it exists in the "tutorial_db" database.

### Task 8: List All in the Table

A script lists all the rows of the "students" table in the "tutorial_db" database.

### Task 9: Class Filter

I created a script that selects and displays specific columns from the "students" table for a class. It allows you to filter data based on the class name.

### Task 10: Class Update

I wrote a script to update the class name for a specific student in the "students" table.

### Task 11: Deleted the Classroom

A script deletes all the data from the "students" table, effectively emptying the table.

### Task 12: Deleted the Classroom-Part 2

A script deletes the "students" table from the "tutorial_db" database.

### Task 13: SQL Injection...

This script demonstrates a security vulnerability known as SQL injection and shows how it can be exploited. It's essential to understand these risks to prevent them in your applications.

### Task 14: Never Leave Your Password in a Comment

This script demonstrates the importance of not leaving passwords or sensitive information in SQL comments.

## Usage

Each task is represented by a separate script. To execute a task, use the MySQL client to run the script.

For example, to perform Task 0:

```bash
$ mysql -h 127.0.0.1 -u root -p < task_0.sql

