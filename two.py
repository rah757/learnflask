from flask import Flask, redirect, url_for, render_template

"""
render_template can be used to link the html file


in html, u can add variable by putting {{}}
here u provided content as name 

in html, inside {} you can actually write python code. just do {% write somewhat native python code here %} 
"""


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",listu=["a", "b", "c"])

@app.route("/<name>") 
def nothome(name): 
    return render_template("index.html",content=name,chick="chicken", listu=["ListE1", "ListE2", "ListE3"]) #render html templates

if __name__ == "__main__":
    app.run()