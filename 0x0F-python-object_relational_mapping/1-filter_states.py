#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa
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
    query = """
            SELECT * FROM states WHERE name
            LIKE BINARY 'N%' ORDER BY states.id
            """
    cursor.execute(query)
    states_with_N = cursor.fetchall()
    for state in states_with_N:
        print(state)

    cursor.close()
    database.close()
