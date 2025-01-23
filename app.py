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
    # Declare vairable
     current_mood = "good"
     friends_list = ['Eliza', 'Courtney', 'Lucian', 'Alex', 'Abby', 'Sohan', 'Grace']
     definitions = {'platypus': 'a blue-green creature that is very good at solving mysteries', 'ladybug': 'an apex predator with magical properties', 'giraffe': 'cunty long neck animal with purple tongue'}
    # Pass Variable into rendered template
     return render_template("about.html", mood = current_mood, friends=friends_list, my_dictionary = definitions)

@app.route("/contact/")
def contact():
     return render_template("contact.html")

# Allows you to click "Run" button
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1117)