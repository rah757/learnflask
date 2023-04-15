from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index1.html", content="testing")

if __name__ == "__main__":
    app.run(debug=True) #debug=true makes sure that u dont have to rerun website server each time u change stuff
