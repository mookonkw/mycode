#!/usr/bin/python3python
#make a FLASK API that just returns a Hello World

from flask import Flask

#app represents our website
app = Flask(__name__)

#decorator
@app.route("/hello/<name>")
def hello_world(name):
    return f"Hello {name.capitalize()}!"

@app.route("/")
def gooverthere():
    return redirect(url_for("hello_world" , name="DefaultUser"))   
    return redirect("/hello/DefaultUser") 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)


