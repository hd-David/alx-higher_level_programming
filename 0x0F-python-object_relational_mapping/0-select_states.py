#!/usr/bin/python3

"""Script to list all states from hbtn_0e_0_usa database"""

import sys
import MySQLdb

if __name__ == "__main__":
    # get command line arguments

    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} username, password database")
        sys.exit(1)

    username, password, database = sys.argv[1:]

    # connect to my MySQL server

    db = MySQLdb.connect( host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    # run a query to fetch all the start and sort by id.

    cursor.execute(" SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    # print all the states

    for state in states:
        print(state)

    db.close()

    
