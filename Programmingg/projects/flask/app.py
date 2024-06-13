from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hackers Poullete</h1><br><a href='/contact'>Contact</a>"

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/submit")
def submit():
    return "<h1>Hackers Poullete</h1><br><a href='/contact'>Contact</a>"

