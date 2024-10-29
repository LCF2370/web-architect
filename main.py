# Imports the Flask Web Framework
from flask import Flask, render_template
# Creates the application instance
app = Flask(__name__)

# Routing
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

# Creates a hosting IP address to run the website
if __name__ == '__main__':
   app.run()