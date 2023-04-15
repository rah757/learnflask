from flask import Flask, redirect, url_for

app = Flask(__name__)
a=False

@app.route("/") #route it to default page (homepage) by giving just /
def home(): #homepage displaying
    return "Hello! This is the main page <h1> Hello there! <h1>" 

@app.route("/<name>")
def user(name):
    return f"hello {name}!" #whatever page the user types, we say "hello name!"

@app.route("/admin")
def admin():
    return redirect(url_for("home")) #redirecting using the redirect fn (if user goes to page.com/admin) that was imported

if __name__ == "__main__":
    app.run()