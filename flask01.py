#!/usr/bin/python3
# An object of Flask class is our WSGI application
import os

from flask import Flask
from flask import jsonify
from flask import request

import yaml
import requests

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/", methods = ["GET"])   # "respond to HTTP GET /"
def hello_world():
   return "Hello World"

@app.route("/astros.json", methods = ["GET"])
def astros():
    return jsonify({"message": "success", "number": 7, "people": [{"craft": "ISS", "name": "Sergey Ryzhikov"}, {"craft": "ISS", "name": "Kate Rubins"}, {"craft": "ISS", "name": "Sergey Kud-Sverchkov"}, {"craft": "ISS", "name": "Mike Hopkins"}, {"craft": "ISS", "name": "Victor Glover"}, {"craft": "ISS", "name": "Shannon Walker"}, {"craft": "ISS", "name": "Soichi Noguchi"}]})


# creates a file called 'converted.yaml' with GET or POST
# also can REMOVE a file 'converted.yaml' with DELETE
@app.route("/jsontoyaml", methods = ["GET", "POST", "DELETE"])
def jsontoyaml():
    if request.method == "DELETE":
        # delete the file if it exists
        if os.path.exists("converted.yaml"):
            os.remove("converted.yaml")
        return "File deleted!"
    elif request.method == "GET":
        urllookup = 'https://www.anapioficeandfire.com/api/books'
    elif request.method == "POST":
        urllookup = request.form['url']
    r = requests.get(urllookup)
    with open("converted.yaml", "w") as cy:
        cy.write(yaml.dump(r.json()))
    return "Conversion complete!"


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
