from flask import Flask
from flask import jsonify
from flask import request
from flask import redirect
from pprint import pprint
import json
import requests 

app = Flask(__name__)

#post classinfo: send python, return JSON
classinfo = {
    "all": [
        {
            "name": "LB",
            "skill level": "outstanding",
            "spirit animal": "Elephant",
            "super power": "Needle Projection",
        },
        {
            "name": "Mabel",
            "skill level": "phenomenal",
            "spirit animal": "Leopard",
            "super power": "Organic Constructs",
        },
        {
            "name": "Pat",
            "skill level": "pleasant",
            "spirit animal": "Albatross",
            "super power": "Prehensile Hair",
        },
        {
            "name": "Shon",
            "skill level": "pleasing",
            "spirit animal": "Alligator",
            "super power": "Prehensile Tail",
        }]}

#new info to be posted to API
newstudent = {
    "name": "NahIla",
    "skill level" : "superhuman",
    "spirit animal": "Raven",
    "super power" : "Shape Shifting"
}

@app.route("/")
def gimmedatdata():
    return jsonify(classinfo)


@app.route("/newstudent", methods = ["POST"])  
def addjson():
        # requests.method
        #requests.format
        # #requests.arg
    data= resuest.json # grab the json inside of an incoming post

    #data will contain the incoming json content
    data_conv = json.loads(data)

    #data_conv is now a python obj
    classinfo["all"].append(data_conv)

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)    