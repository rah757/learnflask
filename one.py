from flask import Flask, redirect, url_for, render_template

"""
render_template can be used to link the html file

"""


app = Flask(__name__)


@app.route("/") #route it to default page (homepage) by giving just /
def home(): #homepage displaying
    return "Hello! This is the main page <h1> Hello there! <h1>" 

@app.route("/<name>")
def user(name):
    return f"hello {name}!" #whatever page the user types, we say "hello name!"

@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="admin!")) #redirecting using the redirect fn that was imported (if user goes to page.com/admin) 
 
if __name__ == "__main__":
    app.run()