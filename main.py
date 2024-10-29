# Imports the Flask Web Framework
from flask import Flask, render_template
# Creates the application instance
app = Flask(__name__)

app = Flask(__name__)

# Routing
@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact")
def contacts():
    return render_template("contact.html")

# Creates a hosting IP address to run the website
if __name__ == '__main__':
   app.run()