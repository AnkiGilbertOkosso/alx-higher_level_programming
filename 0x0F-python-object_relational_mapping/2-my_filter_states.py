#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
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
    sql_query = """SELECT * FROM states WHERE name LIKE BINARY
                '{}'""" .format(sys.argv[4])
    cursor.execute(sql_query)

    matching_states = cursor.fetchall()
    for state in matching_states:
        print(state)
    cursor.close()
    database.close()
