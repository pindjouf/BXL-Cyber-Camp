from datetime import datetime
from flask import Flask
from flask import render_template, request, g
import sqlite3
from markupsafe import escape

app = Flask(__name__)

DATABASE = 'databse'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route("/")
def home():
    return "<h1>Hackers Poullete</h1><br><a href='/contact'>Contact</a>"

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        country = request.form.get("country")
        message = request.form.get("message")
        gender = request.form.get("gender")
        subject = request.form.get("subject")
        action = request.form.get("submit")
        # now = str(datetime.now())
        if action == 'submit':
            get_db()

    return f"Hello, {escape(first_name)}!"

if __name__ == "__main__":
    app.run()
