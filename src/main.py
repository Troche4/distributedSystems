from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/student")
def student():
    return render_template("student.html")

@app.route("/instructor")
def instructor():
    return render_template("instructor.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/session")
def session():
    sessionCode = str()
    for i in range(0,6):
        sessionCode += str(random.randint(0,9))
    return "The code for your session is:" sessionCode


if __name__ == "__main__":
    app.run(debug=True)