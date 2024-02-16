#!/usr/bin/python3
"""
 takes in an argument and
displays all values
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    takes in an argument and
    displays all values
    """
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()
    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
