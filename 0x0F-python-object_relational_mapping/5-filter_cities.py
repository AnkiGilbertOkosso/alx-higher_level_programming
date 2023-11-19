#!/usr/bin/python3
"""
Lists all cities of a given state from the
database hbtn_0e_4_usa (SQL injection free).
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
    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    cities = cursor.fetchall()
    tempo = list(city[0] for city in cities)
    print(*tempo, sep=", ")
    cursor.close()
    database.close()
