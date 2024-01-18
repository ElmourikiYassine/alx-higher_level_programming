#!/usr/bin/python3
"""Script to list states safely based on user
   input from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    (username, password, database, state) = (
            sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=username, passwd=password, db=database)

    cur = db.cursor()

    query = """
    SELECT cities.name
    FROM cities WHERE state_id = (
    SELECT id FROM states WHERE name = %s)
    ORDER BY cities.id"""

    cur.execute(query, (state,))

    rows = cur.fetchall()

    for row in rows:
        print(row[0] , end='')
        print('\n' if rows[len(rows) - 1][0] == row[0] else ', ', end='')
    cur.close()
    db.close()
