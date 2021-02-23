#!/usr/bin/python3
'''     created by: RZFeeser@alta3.com
        description: interact with NASA APIs with python'''
        
# import a library to make HTTP requests and work with JSON response
import requests

# this is the API we want to interact with
NASA = "https://api.nasa.gov/planetary/apod"

def main():
    # get our API key into the program
    # read it out of a file
    with open(r"C:\Users\Galileo\Documents\nasa.creds.txt", "r") as ncreds:
        nc = ncreds.read()
    
    # make the API lookup
    r = requests.get(f"{NASA}?api_key={nc}")
    
    # IF we got back a 200 response...
    if r.status_code == 200:
        # grab JSON off of the 200 response
        nj = r.json()
        
        # print out date        
        print(nj.get("date"))
        
        # print out explanation
        print(nj.get("explanation"))
        
        # print out URL
        print(nj.get("url", "Today's APOD does not have a URL"))
        
    else:
        # ELSE print out we did not get a 200 response back :(
        print(f"Sorry, we got back a {r.status_code}. It appears the API service is down.")

if __name__ == "__main__":
    main()
    input("Press ENTER to exit")