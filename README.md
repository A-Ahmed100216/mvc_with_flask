# MVC with Flask
### Contents
* **MVC**

## MVC
* Model View Controller 

### Display data on the browser using HTML, CSS, JS and Bootstrap
* HTML - Hyper Text Markup Language
* CSS - Cascading Style Sheets 
* JS - JavaScript
* Bootstrap

### Building our API
* Display data rom Python Flask to specific API call/URL/endpoint.

## Why Flask?
* Flask is a web application framework.
* Very powerful to interact with DB and user interfaces/browsers etc.
* Flask can be used to create an API
* It allows us to integrate with HTML, CSS, JS etc.
* Allows us to map HTTP requests to Python functions: URL - HTTP GET 
* Allows us to set the API Path as a URL to view in the browser.
#### Steps
1. Let's install flask
```
pip install flask
``` 
2. Ensure flask is installed.

3. Import relevant packages
```from flask import Flask, jsonify, redirect, url_for```

4. Create an instance of our app
```app = Flask(__name__)```

5. We can create our first route. A decorator will help us to create an API/url for user to access our data in the browser. This will navigate to the localhost:5000. A simple message will be visible on the homepage. 
```python
@app.route("/")  # localhost:5000 this is the default port for Flask

# This function runs when the URL/API is accessed
def home():
    return "<h1>This is a dream team of DevOps Spartans!</hi>"
```

6. Finally set the name to main and set debug to True.
```python
if __name__=="__main__":
    app.run(debug=True)
```
7. To run the flask app:
```python
flask run
```

8. Add more routes and run to test they are working.
```python
# Create a simple dictionary 
students = [
    {"id":0, "title":"Mr","first_name":"Harry","last_name":"Potter", "Course":"Defence Against the DevOps"}
]

# This will add this API/URL to the http://127.0.0.1:5000/api/v1/student/data
@app.route("/api/v1/student/data/", methods=["GET"])
# Apply ETL- Extract Transform Load
def customised_api():
    # jsonify(students) transforms the data in students to JSON
    return jsonify(students)
    
```
```python
# This is a simple welcome page.
@app.route("/welcome/")
def greet_user():
    return "<h1>Welcome to DevOps team</h1>"
```
```python
# This directs to a login page which will redirect to the greet page 
# Ensure the redirect and url_for modules have been imported from flask
@app.route("/login/")
def login():
    # redirect to the greet user page
    return redirect(url_for("greet_user"))
```
```python
# New route for user to input their name 
@app.route("/<username>/")
def welcome_user(username):
    # the welcome string is formatted with the users name to personalise the welcome message. 
    return "<h1>Welcome to DevOps {}</h1>".format(username)
```


 

