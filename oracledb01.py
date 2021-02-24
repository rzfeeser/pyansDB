#!/usr/bin/python3

#required to communicate with OracleDB
import cx_Oracle

def main():
    # Connect string format: [username]/[password]@//[hostname]:[port]/[DB service name]
    conn = cx_Oracle.connect("system/mysecurepassword@//10.5.19.206:51521/XEPDB1")
    
    # create a cursor object
    # required before you make a query
    cur = conn.cursor()

    # this is the command we want to execute
    cur.execute("SELECT 'Hello World!' FROM dual")
    
    # create a response by fetching all data associated with our query
    res = cur.fetchall()
    
    # print our response
    print(res)

if __name__ == "__main__":
    main()

