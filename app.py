# Import relevant packages
from flask import Flask

# Create an instance of our app
app = Flask(__name__)

students = [
    {"id":0, "title":"Mr","first_name":"Harry","last_name":"Potter", "Course":"Defence Against the DevOps"}
]

# Decorator - will help us to create an API/url for user to access our data in the browser.
@app.route("/")  # localhost:5000 this is the default port for Flask

def home():
    return "This is a dream team of DevOps Spartans!"
# This function runs when the URL/API is accessed

if __name__=="__main__":
    app.run(debug=True)