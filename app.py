from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "This is a test1"
    return "This is a test2"