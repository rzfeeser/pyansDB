#!/usr/bin/python3
'''Author: RZFeeser
   Created: 2021-02-22
   Purpose: Interact Python with APIs'''

# python3 -m pip install requests
import requests

# define our constants / globals
ASTRO = "http://api.open-notify.org/astros.json"

def main():
    
    # call the webservice
    resp = requests.get(ASTRO)
    
    # read the JSON off the response 
    oniss = resp.json()
    
    # show off how easy it is to work with our data
    # because this is a dictionary, we can use the ".get()" method
    print(oniss.get("people"))
    
    # pause our script for WINDOWS
    input("Press ENTER to exit.")
    
if __name__ == "__main__":
    main()    
