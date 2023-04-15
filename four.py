from flask import Flask, redirect, url_for, render_template, request 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index2.html")

@app.route("/login", methods=["POST","GET"]) #get is insecure (from link ig) but we use it anyway, post is secure (only saved when sending to database)
def login():
    if request.method == "POST":
        user = request.form["nm"] #req.form is used to access the data from the html. make sure you use POST instead of GET. Req.form is like a dictionary where you can access the value by using the different keys.
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")
    

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)