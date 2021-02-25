#!/usr/bin/python3

import requests

def main():
    # create a response request object called "r"
    # this is the result of sending a POST to http://127.0.0.1:2224/jsontoyaml
    # the attached data attached in a form will be {'url':'http://api.open-notify.org/iss-now.json'}
    #
    # python -------- HTTP DELETE -------> API (http://127.0.0.1:2224/jsontoyaml)
    r = requests.delete("http://127.0.0.1:2224/jsontoyaml")
    # python <------ HTTP 200+txt --------- API (http://127.0.0.1:2224/jsontoyaml)
    # show names inside of r
    print(dir(r))

    # print the status code that was returned
    print(r.status_code)

    # print that the file has been deleted
    print(r.text)

if __name__ == "__main__":
    main()
