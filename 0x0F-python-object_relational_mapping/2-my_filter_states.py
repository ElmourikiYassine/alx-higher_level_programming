#!/usr/bin/python3
"""a script that takes in an argument and displays all
   values in the states table of hbtn_0e_0_usa
    where name matches the argument."""

import sys
import MySQLdb

if __name__ == "__main__":
    (username, password, database, name) = (
            sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database)

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (name,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
