#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms

## resource links
## https://newafrikan77.files.wordpress.com/2016/12/img_1101.jpg
## https://newafrikan77.wordpress.com/2016/12/16/ugwuele-the-ancient-shrine-of-isi-ume-the-origin-of-humankind-igbo-and-the-worship-of-the-great-mother-nnem-chukwu/
## https://www.imodara.com/discover/nigeria-igbo-alusi-spirit-force-figure/

from flask import Flask
from flask import jsonify
from flask import request
from flask import redirect
from pprint import pprint
import json
import requests 

app = Flask(__name__)

global roominfo 

roominfo = { 
    "Hall" : {
        "south" : "South_wing",
        "west"  : "Secret_doorway",
        "east" : "East_wing",
        "item" : "key",
        "desc"  : "==================================================================================================================================================================== \n"    
        "It is a rainy foggy day in the Sacred Grove of Ihu Nne. You are standing in the great hall of Mbari, Great Mother Goddess Alusi Ala\'s shrine. On the wall, there \n" 
        "is a painted figure of Ala, where she balances a child on her knees while she brandishes a sword and is surrounded by the images of other deities, humans and animals. You \n"
        "are Ishindu, the priest and clergy of Ala and your mision is to avert an apocalyspe by finding and sealing the terrifying masqurade Ekwensu in a Ala's womb.  \n"
        "To your south is the South_wing and to your west is a Secret_doorway. You look under the painting and you find a key. \n"
        "============================================================================================================================================================================= "
        },

    "South_wing" : { 
        "north" : "Hall",
        "item"  : ["map", "lantern"],
        "desc" : "================================================================================================================================================================= \n" 
        "You are in the south_wing. There is a large map of the shrine on the wall. On a shelf to the left corner of you, you spy a lantern too. \n"
        "================================================================================================================================================================= "
        },

    "Secret_doorway":{
        "north" : "Hall",
        "item"  : "golden_orb",
        "desc" : "================================================================================================================================================================= \n"
        "you suddenly find yourself in a crypt. \n"
        "================================================================================================================================================================= "
        },

    "East_wing" : {
        "west" : "Hall",
        "south" : "Grove_mouth",
        "item"  : "Ekwensu",
        "desc" : "================================================================================================================================================================= \n"
        "you are in the east wing. be at alert, Ekwensu lurks nearby \n"
        "================================================================================================================================================================= "
        },
    "Grove_mouth" : {
        "north" : "East_wing",
        "desc" : "================================================================================================================================================================= \n"
        "Great work warrior, you have found your way out of the Grove \n"
        "================================================================================================================================================================= "
        }
}

@app.route("/")
def gimmedatdata():
    return jsonify(roominfo)


@app.route("/newroom", methods = ["POST"])  
def addjson():
        # requests.method
        #requests.format
        # #requests.arg
    data= request.json # grab the json inside of an incoming post

    #data will contain the incoming json content
    data_conv = json.loads(data)

    #data_conv is now a python obj
    roominfo["rooms"].append(data_conv)

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2225)    