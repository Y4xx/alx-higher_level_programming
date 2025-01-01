#!/usr/bin/python3
""" script that takes in an argument anddisplays all values
in the states table of hbtn_0e_0_usawhere name matches the argument. """
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    cursor = db.cursor()

    sql_query = "SELECT * FROM states WHERE name = '{}' \
                 ORDER BY id ASC".format(sys.argv[4])

    cursor.execute(sql_query)

    res = cursor.fetchall()

    for row in res:
        if row[1] == sys.argv[4]:
            print(row)
    cursor.close()
    db.close()