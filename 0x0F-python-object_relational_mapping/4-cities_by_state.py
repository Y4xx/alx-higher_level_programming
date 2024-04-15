#!/usr/bin/python3
"""lists all cities"""


import MySQLdb
from sys import argv, exit

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name
                    FROM cities INNER JOIN states
                    ON cities.state_id = states.id""")
    rows = cur.fetchall()

    for data in rows:
        print(data)
    cur.close()
    db.close()
