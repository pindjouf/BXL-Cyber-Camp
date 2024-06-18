from flask import Flask, render_template, request
import sqlite3
import datetime
from dotenv import load_dotenv
import os
import html

app = Flask(__name__)

load_dotenv()

db = os.getenv('DB')

def sanitize(input_str):
    sanitized = html.escape(input_str)
    return sanitized

@app.route("/")
def contact():
    return render_template("contact.html")

@app.post("/submit")
def submit():
    # Make vars and sanitize em
    firstname = sanitize(request.form['first_name'])
    lastname = sanitize(request.form['last_name'])
    email = sanitize(request.form['email'])
    country = sanitize(request.form['country'])
    message = sanitize(request.form['message'])
    gender = sanitize(request.form['gender'])
    subject = sanitize(request.form['subject'])

    # Connect to db
    con = sqlite3.connect(str(db))
    cur = con.cursor()

    # Exec lil insert query
    cur.execute("INSERT INTO contact VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, datetime('now'))", (firstname, lastname, email, country, message, gender, subject))

    con.commit()
    con.close()
    return '<a href="../"><-- Go back</a><br>What up perro I got your data :D'

if __name__ == "__main__":
    app.run()
