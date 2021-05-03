from flask import Flask, render_template

app = Flask(__name__, static_url_path="", static_folder="css/main.css")


@app.route('/')
def hello_world():
    return render_template("index.html")
