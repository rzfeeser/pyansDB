#!/usr/bin/python3
"""Python and MongoDB || by RZFeeser@alta3.com"""

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

def main():
    # connect to MongoDB using the socket we observed mongoDB start on
    client = MongoClient( "mongodb://127.0.0.1:27017/" )
    db=client.admin
    
    # Issue the serverStatus command and print the results
    serverStatusResult=db.command("serverStatus")
    pprint(serverStatusResult)

if __name__ == "__main__":
    main()

