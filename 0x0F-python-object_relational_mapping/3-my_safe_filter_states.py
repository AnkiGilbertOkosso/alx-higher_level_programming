#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where name
matches the argument (safe from MySQL injection).
"""
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(
                host="localhost",
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                port=3306
    )
    cursor = database.cursor()
    search_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (search_name,))
    matching_states = cursor.fetchall()
    for state in matching_states:
        print(state)
    cursor.close()
    database.close()
