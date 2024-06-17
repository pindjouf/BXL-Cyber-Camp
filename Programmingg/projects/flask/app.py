from flask import Flask, render_template, request
import sqlite3
import datetime
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

db = os.getenv('DB')

@app.route("/")
def contact():
    return render_template("contact.html")

@app.post("/submit")
def submit():
    # Connect to db
    con = sqlite3.connect(str(db))
    cur = con.cursor()

    # Exec lil insert query
    cur.execute("INSERT INTO contact VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, datetime('now'))", (request.form['first_name'], request.form['last_name'], request.form['email'], request.form['country'], request.form['message'], request.form['gender'], request.form['subject']))

    # Commit the query to db
    con.commit()
    con.close()
    return '<a href="../">Go back :D</a><br>What up perro I got your data'

if __name__ == "__main__":
    app.run()
