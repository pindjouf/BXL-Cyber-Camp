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
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    country = request.form.get("country")
    message = request.form.get("message")
    gender = request.form.get("gender")
    subject = request.form.get("subject")

    if request.method == 'POST':

    return "<h1>Hackers Poullete</h1><br><a href='/contact'>Contact</a>"

if __name__ == "__main__":
    app.run()
