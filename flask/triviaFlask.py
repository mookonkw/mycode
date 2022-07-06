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

@app.route("/correct", methods = ["POST", "GET"])
def success():
    if request.form.get("nm") == "female":
        return f"The answer is : " + request.form.get("nm")
    else :
        return redirect(url_for("start"))    

#This is a landing point for users (a start)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("postmaker.html") # look for templates/postmaker.html


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2225) # runs the application
