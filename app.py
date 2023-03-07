from flask import Flask, render_template, request, redirect, jsonify,url_for
import webbrowser
import pandas as pd
from datetime import datetime
import json
from predict import predict_offer
from charts import bar_chart, pie_chart, polar_area, revenue_chart, metrics, radial_chart, stacked
import numpy as np
import csv
from plot import comparative_plot

# Create Flask app
app = Flask(__name__)


# Define home route
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     global name, email_id, phone
#     if request.method == 'POST':
#         # Get the form input values
#         name = request.form['name']
#         email_id = request.form['email']
#         phone = request.form['phone']
#
#         return render_template('index.html')
#     else:
#         # Render the form template
#         return render_template('login.html')

# Function to register a user
def register_user(name, phone, email, password, address):
    # Write the user data to a CSV file
    with open("database/users.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email, password, address])


def authenticate_user(email, password):
    global name, email_id, phone
    df = pd.read_csv("database/users.csv", header=None, names=["Name","Phone", "Email", "Password", "Address"])
    if email in df['Email'].values:
        index = df.index[df['Email'] == email].tolist()[0]
        email_id = df.at[index, 'Email']
        name = df.at[index, 'Name']
        phone = df.at[index, 'Phone']
        if df.at[index, 'Password'] == password:
            return True
        else:
            return False
    else:
        return False


# Route for the registration page
@app.route("/register", methods=["GET", "POST"])
def register():
    global name, email_id, phone
    if request.method == "POST":
        # Get the user data from the form
        name = request.form["signupname"]
        phone = request.form["signupphone"]
        email_id = request.form["signupemail"]
        password = request.form["signuppassword"]
        address = request.form["signupaddr"]

        # Register the user
        register_user(name, phone, email_id, password, address)

        # Redirect the user to the login page
        return redirect(url_for("login"))
    else:
        return render_template("login2.html")


# Route for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    global name, email_id, phone
    if request.method == "POST":
        # Get the user data from the form
        email_id = request.form["loginemail"]
        password = request.form["loginpassword"]

        # Authenticate the user
        if authenticate_user(email_id, password):
            return render_template('index.html')
        else:
            return "Login failed"
    else:
        return render_template("login2.html")


@app.route('/booking', methods=['POST'])
def booking():
    global movie_name, cost, offer
    data = request.get_json()
    movie_name = data['movie_name']
    cost = data['cost']
    offer = data['offer']
    print(movie_name)
    print("Tickets Booked!!")
    return render_template('index.html', movie_name=movie_name, cost=cost, offer=offer)


@app.route('/booked', methods=['GET', 'POST'])
def booked():
    # Get the current date and time
    now = datetime.now()

    # Extract the current year, month, and day
    year = now.year
    month = now.month
    day = now.day

    # Extract the current hour, minute, and second
    hour = now.hour
    minute = now.minute
    second = now.second

    # Print the current date and time in the format YYYY-MM-DD HH:MM:SS
    date = f"{day:02d}-{month:02d}-{year}"
    time = f"{hour:02d}:{minute:02d}:{second:02d}"
    # Define the data to be added
    data = {'name': name,
            'email_id': email_id,
            'phone': phone,
            'movie_name': movie_name,
            'cost': cost,
            'offer': offer,
            'date': date,
            'time': time}

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data, index=[0])

    # Open the CSV file in append mode
    with open('database/dataset.csv', 'a', newline='') as f:
        df.to_csv(f, header=False, index=False)
    return render_template('booked.html', movie_name=movie_name)


@app.route('/blog_details', methods=['GET', 'POST'])
def blog_details():
    return render_template('blog_details.html')


@app.route('/celebrities', methods=['GET', 'POST'])
def celebrities():
    return render_template('celebrities.html')


@app.route('/index_2', methods=['GET', 'POST'])
def index_2():
    return render_template('index.html')


@app.route('/movie_details', methods=['GET', 'POST'])
def movie_details():
    print(f"Got the name {movie_name}")
    return render_template('movie_details.html', movie_name=movie_name)


@app.route('/movies', methods=['GET', 'POST'])
def movies():
    return render_template('movies.html')


@app.route('/top_movies', methods=['GET', 'POST'])
def top_movies():
    return render_template('top_movies.html')


@app.route('/landing', methods=['GET', 'POST'])
def landing():
    return render_template('landing.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    total_sales, total_revenue, total_customers = metrics()
    bar_chart_data = bar_chart()
    pie_chart_data = pie_chart()
    polar_area_data = polar_area()
    value, labels = revenue_chart()
    rc_labels, rc_data, rc_sales = radial_chart()
    s_labels, s_cost, s_real_cost = stacked()
    return render_template('dashboard.html', bar_chart_data=bar_chart_data, pie_chart_data=pie_chart_data,
                           polar_area_data=polar_area_data, value=value, labels=labels, rc_labels=rc_labels,
                           rc_data=rc_data, rc_sales=rc_sales, s_labels=s_labels, s_cost=s_cost,
                           s_real_cost=s_real_cost, total_sales=total_sales, total_revenue=total_revenue,
                           total_customers=total_customers)


@app.route('/charts1', methods=['GET', 'POST'])
def charts1():
    bar_chart_data = bar_chart()
    pie_chart_data = pie_chart()
    polar_area_data = polar_area()
    value, labels = revenue_chart()
    rc_labels, rc_data, rc_sales = radial_chart()
    s_labels, s_cost, s_real_cost = stacked()
    return render_template('charts1.html', bar_chart_data=bar_chart_data, pie_chart_data=pie_chart_data,
                           polar_area_data=polar_area_data, value=value, labels=labels, rc_labels=rc_labels,
                           rc_data=rc_data, rc_sales=rc_sales, s_labels=s_labels, s_cost=s_cost,
                           s_real_cost=s_real_cost)


@app.route('/charts2', methods=['GET', 'POST'])
def charts2():
    value, labels = revenue_chart()
    return render_template('charts2.html', value=value, labels=labels)


@app.route('/charts3', methods=['GET', 'POST'])
def charts3():
    return render_template('charts3.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
    return render_template('results.html')


@app.route('/algo_stats', methods=['GET', 'POST'])
def algo_stats():
    return render_template('algo_stats.html')



@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    global moviename, offer_DTR, offer_LR, offer_KNR, offer_RFR, offer_SVR, offer_GBR
    if request.method == "POST":
        moviename = request.form.get("moviename")

        ticket_cost = request.form.get("ticket_cost")
        sales = request.form.get("sales")
        print(ticket_cost, sales)
        input = np.array([int(ticket_cost), int(sales)])
        input = input.reshape(1, -1)

        offer_LR, offer_GBR, offer_KNR, offer_DTR, offer_RFR, offer_SVR = predict_offer(input)

    return render_template('results.html', moviename=moviename, offer_LR=offer_LR, offer_GBR=offer_GBR, offer_KNR=offer_KNR,
                           offer_DTR=offer_DTR, offer_RFR=offer_RFR, offer_SVR=offer_SVR)


# Function to open a CSV file and return its data as a list
def open_csv(filepath, filename):
    with open(filepath + filename, mode='r') as file:
        csvFile = csv.reader(file)

        for lines in csvFile:
            arr = lines

        data = list(arr)
        return data


# ---------------------------------------- Metrics Display ------------------------------------------------------------

def default_metrics_display(name):
    # filename is the name of the CSV file for the given algorithm
    filename = f'stats_{name}.csv'
    # data is the contents of the CSV file
    data = open_csv('static/assets/csv/', filename)

    print(data)
    f = f'static/assets/csv/stats_{name}.csv'
    # data_csv is a list of rows in the CSV file
    data_csv = []
    with open(f) as file:
        csvfile = csv.reader(file)
        for row in csvfile:
            data_csv.append(row)

    # data_csv is converted to a Pandas DataFrame
    data_csv = pd.DataFrame(data_csv)

    # img_name is the name of the image file for the given algorithm
    img_name = f'stats_{name}.png'
    cnf = f'plot_{name}.png'
    return filename, img_name, data_csv, cnf


# These functions handle requests to display statistics for a particular algorithm
@app.route('/stats_DTR')
def stats_DTR():
    name = "DTR"
    filename, img_name, data_csv, cnf = default_metrics_display(name)
    if ".csv" in filename:
        # Render an HTML template with the data for the given algorithm
        return render_template('algo_stats.html', algo=name, img=img_name, cnf=cnf,
                               data=data_csv.to_html(classes='mystyle', header=False, index=False))
    else:
        return render_template('index.html')

@app.route('/stats_GBR')
def stats_GBR():
    name = "GBR"
    filename, img_name, data_csv, cnf = default_metrics_display(name)
    if ".csv" in filename:
        # Render an HTML template with the data for the given algorithm
        return render_template('algo_stats.html', algo=name, img=img_name, cnf=cnf,
                               data=data_csv.to_html(classes='mystyle', header=False, index=False))
    else:
        return render_template('index.html')

@app.route('/stats_KNR')
def stats_KNR():
    name = "KNR"
    filename, img_name, data_csv, cnf = default_metrics_display(name)
    if ".csv" in filename:
        # Render an HTML template with the data for the given algorithm
        return render_template('algo_stats.html', algo=name, img=img_name, cnf=cnf,
                               data=data_csv.to_html(classes='mystyle', header=False, index=False))
    else:
        return render_template('index.html')

@app.route('/stats_LR')
def stats_LR():
    name = "LR"
    filename, img_name, data_csv, cnf = default_metrics_display(name)
    if ".csv" in filename:
        # Render an HTML template with the data for the given algorithm
        return render_template('algo_stats.html', algo=name, img=img_name, cnf=cnf,
                               data=data_csv.to_html(classes='mystyle', header=False, index=False))
    else:
        return render_template('index.html')

@app.route('/stats_RFR')
def stats_RFR():
    name = "RFR"
    filename, img_name, data_csv, cnf = default_metrics_display(name)
    if ".csv" in filename:
        # Render an HTML template with the data for the given algorithm
        return render_template('algo_stats.html', algo=name, img=img_name, cnf=cnf,
                               data=data_csv.to_html(classes='mystyle', header=False, index=False))
    else:
        return render_template('index.html')

@app.route('/stats_SVR')
def stats_SVR():
    name = "SVR"
    filename, img_name, data_csv, cnf = default_metrics_display(name)
    if ".csv" in filename:
        # Render an HTML template with the data for the given algorithm
        return render_template('algo_stats.html', algo=name, img=img_name, cnf=cnf,
                               data=data_csv.to_html(classes='mystyle', header=False, index=False))
    else:
        return render_template('index.html')

# ----------------------------------------------------------------------------------------------------

# This function handles requests for the comparative analysis page
@app.route('/comparative_analysis', methods=['GET', 'POST'])
def comparative_analysis():
    # compare_data is a Pandas DataFrame containing the comparison data for the different algorithms
    compare_data = comparative_plot(offer_DTR,
                        offer_GBR,
                        offer_KNR,
                        offer_LR,
                        offer_RFR,
                        offer_SVR)

    # Render the comparative analysis HTML template with the comparison data
    return render_template('comparative_analysis.html',
                           compare_data=compare_data.to_html(classes='mystyle', index=False))


if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:5000/landing')
    app.run(debug=True, port=5000)
