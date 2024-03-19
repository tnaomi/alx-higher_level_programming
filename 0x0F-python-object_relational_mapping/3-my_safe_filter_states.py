#!/usr/bin/python3
'''
script that takes in an argument and displays all values in the states
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost')

    curs = db.cursor()
    curs.execute('SELECT * from states WHERE name = %s ORDER BY states.id',
                   (sys.argv[4], ))

    states = curs.fetchall()
    for state in states:
        print(state)

    curs.close()
    db.close()
