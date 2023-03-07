# import csv
# import random
# import datetime
#
# # list of movie names, costs, and offers
# movies = [["Super 30", 250, 20], ["Radhe", 300, 10], ["3 Idiots", 200, 0], ["Avatar", 400, 0], ["Bhediya", 150, 10],
#           ["Pushpa", 200, 25], ["ABCD", 250, 15], ["KGF", 300, 5], ["Circus", 500, 20], ["Brahmastra", 350, 12]]
#
# # open the CSV file in append mode
# with open('database/create.csv', 'a', newline='') as csvfile:
#     # create a CSV writer object
#     writer = csv.writer(csvfile)
#
#     # generate 30 random entries and append them to the CSV file
#     for i in range(500):
#         # generate a random movie from the list
#         movie = random.choice(movies)
#         movie_name = movie[0]
#         cost = movie[1]
#         offer = movie[2]
#
#         # generate a random name, email, phone, and date/time
#         name = f"Person{i + 1}"
#         email = f"{name.lower()}@gmail.com"
#         phone = f"9{random.randint(1000000000, 9999999999)}"
#         date = datetime.datetime.now().strftime("%d-%m-%Y")
#         time = datetime.datetime.now().strftime("%H:%M:%S")
#
#         # write the data to the CSV file
#         writer.writerow([name, email, phone, movie_name, cost, offer, date, time])


import csv
import random
import datetime

# list of movie names, costs, and offers
movies = [["Super 30", 250, 20], ["Radhe", 300, 10], ["3 Idiots", 200, 0], ["Avatar", 400, 0], ["Bhediya", 150, 10],
          ["Pushpa", 200, 25], ["ABCD", 250, 15], ["KGF", 300, 5], ["Circus", 500, 20], ["Brahmastra", 350, 12]]

# open the CSV file in append mode
with open('database/create2.csv', 'a', newline='') as csvfile:
    # create a CSV writer object
    writer = csv.writer(csvfile)

    for i in range(500):
        # generate a random movie from the list
        movie = random.choice(movies)
        movie_name = movie[0]
        cost = movie[1]
        offer = movie[2]

        # generate a random name, email, phone, and date/time
        name = f"Person{i + 1}"
        email = f"{name.lower()}@gmail.com"
        phone = f"9{random.randint(1000000000, 9999999999)}"
        date = datetime.datetime.now().strftime("%d-%m-%Y")
        time = datetime.datetime.now().strftime("%H:%M:%S")

        # determine the likelihood of booking based on the offer
        likelihood = 0
        if offer >= 22:
            likelihood = 1
        elif offer >= 20:
            likelihood = random.uniform(0.9, 1)
        elif offer >= 15:
            likelihood = random.uniform(0.7, 0.9)
        elif offer >= 10:
            likelihood = random.uniform(0.5, 0.7)
        elif offer >= 5:
            likelihood = random.uniform(0.3, 0.5)
        elif offer >= 0:
            likelihood = random.uniform(0.1, 0.3)

        # decide whether to book a ticket based on the likelihood
        if random.uniform(0, 1) <= likelihood:
            # write the data to the CSV file
            writer.writerow([name, email, phone, movie_name, cost, offer, date, time])

import csv
import pandas as pd

# Create an empty dictionary to store the movie names, costs, and real costs
movies = {}

# Read the data from the CSV file and store it in a dictionary
with open('database/create2.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movie_name = row['movie_name']
        cost = int(row['cost'])
        offer = int(row['offer'])
        price = cost * (1 - offer / 100)

        # Calculate the real cost by applying the offer
        real_cost = cost - (cost * offer) / 100

        # Add the movie name, cost, and real cost to the dictionary
        if movie_name not in movies:
            movies[movie_name] = {'cost': cost, 'real_cost': real_cost, 'offer': offer, 'revenue': price, 'sales': 1}
        else:
            movies[movie_name]['revenue'] += price
            movies[movie_name]['sales'] += 1

# Extract the movie names, costs, real costs, offers, revenues, and sales from the dictionary
labels = []
costs = []
real_costs = []
offers = []
revenues = []
sales = []
for movie_name, details in movies.items():
    labels.append(movie_name)
    costs.append(details['cost'])
    real_costs.append(details['real_cost'])
    offers.append(details['offer'])
    revenues.append(details['revenue'])
    sales.append(details['sales'])

# Create a DataFrame from the movie names, costs, real costs, offers, revenues, and sales
df = pd.DataFrame({"movie_name": labels, "cost": costs, "real_cost": real_costs, "offer": offers, "revenue": revenues, "sales": sales})

# Display the resulting DataFrame
print(df)