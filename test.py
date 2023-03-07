import csv
import webbrowser

import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Function to register a user
def register_user(phone, email, password, address):
    # Write the user data to a CSV file
    with open("database/users.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([phone, email, password, address])


def authenticate_user(email, password):
    df = pd.read_csv("database/users.csv", header=None, names=["Phone", "Email", "Password", "Address"])
    if email in df['Email'].values:
        index = df.index[df['Email'] == email].tolist()[0]
        if df.at[index, 'Password'] == password:
            return True
        else:
            return False
    else:
        return False


# Route for the registration page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Get the user data from the form
        phone = request.form["signupphone"]
        email = request.form["signupemail"]
        password = request.form["signuppassword"]
        address = request.form["signupaddr"]

        # Register the user
        register_user(phone, email, password, address)

        # Redirect the user to the login page
        return redirect(url_for("login"))
    else:
        return render_template("login2.html")


# Route for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get the user data from the form
        email = request.form["loginemail"]
        password = request.form["loginpassword"]

        # Authenticate the user
        if authenticate_user(email, password):
            return "Login successful"
        else:
            return "Login failed"
    else:
        return render_template("login2.html")

# Define home route
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:8000/login')
    app.run(debug=True, port=8000)

