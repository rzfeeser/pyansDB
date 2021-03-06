#!/usr/bin/python3

import requests

def main():
    # create a response request object called "r"
    # this is the result of sending a POST to http://127.0.0.1:2224/jsontoyaml
    # the attached data attached in a form will be {'url':'http://api.open-notify.org/iss-now.json'}
    #
    # python -------- HTTP POST+form -------> API (http://127.0.0.1:2224/jsontoyaml)
    r = requests.post("http://127.0.0.1:2224/jsontoyaml", data = {'url':'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY'})
    # python <------ HTTP 200+json --------- API (http://127.0.0.1:2224/jsontoyaml)
    # show names inside of r
    print(dir(r))

    # print the status code that was returned
    print(r.status_code)

if __name__ == "__main__":
    main()
