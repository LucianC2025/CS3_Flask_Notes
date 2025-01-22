from flask import Flask 
from flask import render_template

# Create a flask instance and assign it to variable app
app = Flask(__name__)

# Create a route (think: "what should this browser load when something happens" its like a path to a specific page)
# Index route for web app (homepage) (think: "What do you see when you first load up this page")
@app.route("/")
def index():
    #return "Hello world!"
    return render_template('index.html')

@app.route("/hello/")
@app.route("/hello/<name_data>")
def hello_there(name_data = None):
    return render_template("hello_there.html", name=name_data)


@app.route("/api/data/")
def get_data():
    # Displays data file returned from an API call
    # can do more Python work to format this later
    return app.send_static_file("data.json")

@app.route("/about/")
def about():
     return render_template("about.html")

@app.route("/contact/")
def contact():
     return render_template("contact.html")

# Allows you to click "Run" button
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1117)