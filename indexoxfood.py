from flask import Flask
from flask import render_template

app = Flask("MyApp")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/orielcollege")
def oriel():
    return render_template("orielcollege.html")

app.run(debug=True)
