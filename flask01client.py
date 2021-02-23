#!/usr/bin/python3

import requests

def main():
    r = requests.post("http://127.0.0.1:2224/jsontoyaml", data = {'url':'http://api.open-notify.org/iss-now.json'})

if __name__ == "__main__":
    main()