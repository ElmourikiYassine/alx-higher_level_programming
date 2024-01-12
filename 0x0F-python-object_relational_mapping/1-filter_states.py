#!/usr/bin/python3
"""Script to list states with names
   starting with 'N' from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
