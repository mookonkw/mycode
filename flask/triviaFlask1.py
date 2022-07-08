#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)
## This is where we want to redirect users to

#grab the value 'username'
@app.route("/start/<username>")
def index(username):
    # render the jinja template "helloname.html"
    # apply the value of username for the var name
    return render_template("helloname.html", user = username.capitalize())


@app.route("/answer", methods = ["POST", "GET"])
def success():
    if request.form.get("nm") == "female":
        return f"Correct. The answer is : " + request.form.get("nm")
    else :
        return f"Sorry. Thats not quite right :("

#This is a landing point for users (a start)
#@app.route("/") # user can land at "/"
@app.route("/start/<username>") # or user can land at "/start"
def start():
    return render_template("postmaker.html") # look for templates/postmaker.html



if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
