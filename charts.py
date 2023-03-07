import csv
import numpy as np
import json


def bar_chart():
    # read the data from the CSV file
    with open('database/dataset.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    # extract the movie names and ticket sales
    movie_names = [row['movie_name'] for row in data]

    # analyze the popularity of different movies
    movie_counts = {}
    for movie in movie_names:
        if movie in movie_counts:
            movie_counts[movie] += 1
        else:
            movie_counts[movie] = 1

    # create a bar chart to visualize the popularity of different movies
    labels = list(movie_counts.keys())
    data = list(movie_counts.values())

    # define the data to be passed to the JavaScript function
    data = {
        'labels': labels,
        'datasets': [{
            'label': 'Tickets sold',
            'data': data,
            'backgroundColor': ['rgba(255, 99, 132, 0.2)', 'rgba(255, 159, 64, 0.2)', 'rgba(255, 205, 86, 0.2)',
                                'rgba(75, 192, 192, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(153, 102, 255, 0.2)',
                                'rgba(201, 203, 207, 0.2)'],
            'borderColor': ['rgb(255, 99, 132)', 'rgb(255, 159, 64)', 'rgb(255, 205, 86)', 'rgb(75, 192, 192)',
                            'rgb(54, 162, 235)', 'rgb(153, 102, 255)', 'rgb(201, 203, 207)'],
            'borderWidth': 1
        }]
    }

    # encode the data as a JSON object
    json_data = json.dumps(data)
    return json_data


def pie_chart():
    with open('database/dataset.csv', 'r') as csvfile:
        # use a DictReader object instead of a reader object
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    # analyze the popularity of different movies
    movie_counts = {}
    movie_names = [row['movie_name'] for row in data]
    for movie in movie_names:
        if movie in movie_counts:
            movie_counts[movie] += 1
        else:
            movie_counts[movie] = 1

    value = list(movie_counts.values())
    labels = list(movie_counts.keys())

    data = {
        'labels': labels,
        'datasets': [{
            'label': 'Tickets sold',
            'data': value,
            'backgroundColor': ['rgba(255, 99, 132, 1)', 'rgba(255, 159, 64, 1)', 'rgba(255, 205, 86, 1)',
                                'rgba(75, 192, 192, 1)', 'rgba(54, 162, 235, 1)', 'rgba(153, 102, 255, 1)',
                                'rgba(201, 203, 207, 1)'],
            'hoverOffset': 4
        }]
    }

    # encode the data as a JSON object
    json_data = json.dumps(data)
    return json_data




def polar_area():
    with open('database/dataset.csv', 'r') as csvfile:
        # use a DictReader object instead of a reader object
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    # extract the movie names, costs, and offers
    # use the keys of the dictionary to access the values
    movie_names = [row['movie_name'] for row in data]
    costs = [row['cost'] for row in data]
    offers = [row['offer'] for row in data]
    # analyze the impact of offers on ticket sales
    offer_counts = {}
    for offer in offers:
        if offer in offer_counts:
            offer_counts[offer] += 1
        else:
            offer_counts[offer] = 1

    value = list(offer_counts.values())
    labels = list(offer_counts.keys())
    true = []
    for i in labels:
        string = i + "% off"
        true.append(string)

    data = {
        'labels': true,
        'datasets': [{
            'label': 'Tickets Sold',
            'data': value,
            'backgroundColor': [
                'rgb(255, 99, 132)',
                'rgb(75, 192, 192)',
                'rgb(255, 205, 86)',
                'rgb(201, 203, 207)',
                'rgb(54, 162, 235)'
            ]
        }]
    }
    # encode the data as a JSON object
    json_data = json.dumps(data)
    return json_data


def revenue_chart():
    revenue = {}

    with open('database/dataset.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            movie_name = row['movie_name']
            cost = int(row['cost'])
            offer = int(row['offer'])
            price = cost * (1 - offer / 100)

            # if the movie is not in the dictionary, add it and set the revenue to the price of the ticket
            if movie_name not in revenue:
                revenue[movie_name] = price
            # if the movie is already in the dictionary, add the price of the ticket to the existing revenue
            else:
                revenue[movie_name] += price

    value = list(revenue.values())
    labels = list(revenue.keys())


    return value, labels


def metrics():
    # read the data from the CSV file
    with open('database/dataset.csv', 'r') as csvfile:
        # use a DictReader object instead of a reader object
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    # extract the movie names, costs, and offers
    # use the keys of the dictionary to access the values
    movie_names = [row['movie_name'] for row in data]
    costs = [row['cost'] for row in data]
    email_ids = [row['email_id'] for row in data]

    # calculate the total number of tickets sold
    total_sales = len(movie_names)

    # calculate the total revenue
    total_revenue = sum(int(cost) for cost in costs)

    # calculate the total number of customers
    total_customers = len(set(email_ids))

    print("Total sales:", total_sales)
    print("Total revenue:", total_revenue)
    print("Total customers:", total_customers)
    return total_sales, total_revenue, total_customers


def radial_chart():
    # read the data from the CSV file
    with open('database/dataset.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    # extract the movie names and ticket sales
    movie_names = [row['movie_name'] for row in data]

    # analyze the popularity of different movies
    movie_counts = {}
    for movie in movie_names:
        if movie in movie_counts:
            movie_counts[movie] += 1
        else:
            movie_counts[movie] = 1

    # create a bar chart to visualize the popularity of different movies
    labels = list(movie_counts.keys())
    data = list(movie_counts.values())

    sales = sum(data)
    return labels, data, sales

def stacked():
    with open('database/dataset.csv', 'r') as csvfile:
        # use a DictReader object to read the data
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    # create a dictionary to store the movie names, costs, and real costs
    movies = {}

    for row in data:
        movie_name = row['movie_name']
        cost = int(row['cost'])
        offer = int(row['offer'])

        # calculate the real cost by applying the offer
        real_cost = cost - (cost * offer) / 100

        # add the movie name, cost, and real cost to the dictionary
        if movie_name not in movies:
            movies[movie_name] = {'cost': cost, 'real_cost': real_cost}

    # print the movie names, costs, and real costs
    labels = []
    cost = []
    real_cost = []
    for movie_name, details in movies.items():

        labels.append(movie_name)

        cost.append(details['cost'])

        real_cost.append(details['real_cost'])

    print(labels)
    print(cost)
    print(real_cost)
    return labels, cost, real_cost


