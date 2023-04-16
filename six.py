from flask import Flask, redirect, url_for, render_template, request, session, flash 
from datetime import timedelta

app = Flask(__name__)

app.secret_key = "chickenfry"

app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index2.html")

@app.route("/login", methods=["POST","GET"]) #get is insecure (from link ig) but we use it anyway, post is secure (only saved when sending to database)
def login():
    if request.method == "POST":
        session.permanent = True #set session to last as long as defined using the datetime timedelta function
        user = request.form["nm"] #req.form is used to access the data from the html. make sure you use POST instead of GET. Req.form is like a dictionary where you can access the value by using the different keys.
        session["user"] = user
        flash("Login successful!")
        return redirect(url_for("user",usr=user))
    else:
        if "user" in session:
            flash("Already logged in")
            return redirect(url_for("user"))
        return render_template("login.html")
    

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in")
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    session.pop("user", None) #remove the current session essentially making them logout
    if "user" in session:
        user = session["user"]
        flash("You have been logged out successfully, {user}", "info") #flash function is used to flash a message whenever this function takes place. "info" here is a category that shows the 'i' icon aside
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)