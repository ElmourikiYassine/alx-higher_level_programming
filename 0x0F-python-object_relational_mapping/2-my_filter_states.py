#!/usr/bin/python3
"""Script to list states safely based on user
   input from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    (username, password, database, user_input) = (
            sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=username, passwd=password, db=database)

    cur = db.cursor()

    query = """
    SELECT * FROM states
    WHERE name
    LIKE BINARY '{}'
    ORDER BY states.id ASC"""
    query = query.format(user_input)

    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
