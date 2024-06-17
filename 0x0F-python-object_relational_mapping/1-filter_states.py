#!/usr/bin/python3
""" takes in an argument
    and displays all values
    in the states table of
    hbtn_0e_0_usa where name matches the argument
     Usage: ./2-my_filter_states.py <mysql username>
                                    <mysql password>
                                    <database name>
                                    <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT * \
                    FROM states \
                    WHERE CONVERT(`name` USING Latin1) \
                    COLLATE Latin1_General_CS \
                    LIKE 'N%';")
    states = curs.fetchall()
    for state in states:
        print(state)
    curs.close()
    db.close()
