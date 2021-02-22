#!/usr/bin/python3
'''Author: RZFeeser
   Created: 2021-02-22
   Purpose: Interact Python with APIs'''


# std library for interacting with URIs (usually HTTP)
import urllib.request

# std library for interacting with JSON
import json

# define our constants / globals
ASTRO = "http://api.open-notify.org/astros.json"

def main():
    
    # call the webservice
    resp = urllib.request.urlopen(ASTRO)
    
    # read the JSON off the respons (this produces a bytes object)
    resp = resp.read()
    
    # decode bytes object to str
    respstr = resp.decode("utf-8")
    
    # convert str to pythonic dict and lists
    oniss = json.loads(respstr)
    
    # show off how easy it is to work with our data
    # because this is a dictionary, we can use the ".get()" method
    print(oniss.get("people"))
    
    # pause our script for WINDOWS
    input("Press ENTER to exit.")
    
if __name__ == "__main__":
    main()    