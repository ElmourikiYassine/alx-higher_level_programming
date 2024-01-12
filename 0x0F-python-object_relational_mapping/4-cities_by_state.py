#!/usr/bin/python3
"""Script to list states safely based on user
   input from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    (username, password, database) = (
            sys.argv[1], sys.argv[2], sys.argv[3])

    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=username, passwd=password, db=database)

    cur = db.cursor()

    cur.execute("""
    SELECT cities.id, cities.name, states.name
    FROM cities JOIN states
    ON cities.state_id = states.id ORDER BY cities.id""")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
