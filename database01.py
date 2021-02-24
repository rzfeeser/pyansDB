#!/usr/bin/python3

import sqlite3


def main():
    # connect to test.db
    # if test.db does not exist
    # then create it
    conn = sqlite3.connect('test.db')
    
    print("Opened database successfully")

    conn.execute('''CREATE TABLE COMPANY
 (ID INT PRIMARY KEY     NOT NULL,
 NAME           TEXT    NOT NULL,
 AGE            INT     NOT NULL,
 ADDRESS        CHAR(50),
 SALARY         REAL);''')

    print("Table created successfully")


if __name__ == "__main__":
    main()
