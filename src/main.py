from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/student")
def student():
    return render_template("student.html", methods=["GET","POST"])

@app.route("/instructor", methods=["GET","POST"])
def instructor():
    return render_template("instructor.html")

@app.route("/create", methods=["GET","POST"])
def create():
    return render_template("create.html")

@app.route("/session", methods=["GET","POST"])
def session():
    sessionCode = str()
    for i in range(0,6):
        sessionCode += str(random.randint(0,9))
    return render_template("session.html", output = sessionCode)


if __name__ == "__main__":
    app.run(debug=True)