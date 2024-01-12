#!/usr/bin/python3

import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], host='localhost:3306', database=sys.argv[3])
cursor = db.cursor()

cursor.execute("SELECT names FROM states ORDER BY id ASC")

rows = cursor.fetchall()
for row in rows:
    print(row)


