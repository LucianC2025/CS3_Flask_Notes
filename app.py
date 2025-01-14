from flask import Flask 

# Create a flask instance and assign it to variable app
app = Flask(__name__)

# Create a route (think: "what should this browser load when something happens" its like a path to a specific page)
# Index route for web app (homepage) (think: "What do you see when you first load up this page")
@app.route("/")
def index():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9874)