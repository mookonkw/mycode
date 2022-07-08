#!/usr/bin/python3

from pprint import pprint
import json
import requests 

#url to send newroom to
url = "http://127.0.0.1:2225"

#new info to be posted to API
roominfo = {"Sacred_chamber" : {
    "west" : "South_wing",
    "item": "taxidermed Raven",
    "desc" : "Ala and Amadioha will speak to you here"
}
}

#converting newroom to json

#specifying newroom as the JSON we are posting
post_resp = requests.post(url + "/newroom", json=json.dumps(newroom))

pprint(post_resp.text)
