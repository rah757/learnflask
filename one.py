from flask import Flask

app = Flask(__name__)

@app.route("/") #route it to default page (homepage) by giving just /
def home(): #homepage displaying
    return "Hello! This is the main page <h1> Hello there! <h1>" 

if __name__ == "__main__":
    app.run()