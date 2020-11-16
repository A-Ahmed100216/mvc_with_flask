# Import relevant packages
from flask import Flask, jsonify

# Create an instance of our app
app = Flask(__name__)

students = [
    {"id":0, "title":"Mr","first_name":"Harry","last_name":"Potter", "Course":"Defence Against the DevOps"}
]

# Decorator - will help us to create an API/url for user to access our data in the browser.
@app.route("/")  # localhost:5000 this is the default port for Flask

def home():
    return "<h1>This is a dream team of DevOps Spartans!</hi>"
# This function runs when the URL/API is accessed


# Creating our own API to display data on the specific route/URL/endpoint.
@app.route("/api/v1/student/data", methods=["GET"])
# This will add this API/URL to the http://127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(students)
    # Apply ETL- Extract Transform Load
    # jsonify(students) transforms the data in students to JSON



if __name__=="__main__":
    app.run(debug=True)