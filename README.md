# Movie Analytics
Movie Analytics is a web-based project that provides a comprehensive solution for movie booking and analysis. The project has a landing page that provides two options for clients to book a movie and for admin to view analytics.

## Demo

https://user-images.githubusercontent.com/63944541/223365547-510262fc-150f-4c76-b097-f9fbe44e2c74.mp4



This project offers a full solution for movie analytics, with a landing page, client page, and admin 

**The landing page provides two options for the users - client to book a movie and admin to view analytics.**
- ![App Screenshot](https://github.com/prathameshparit/Dummy-Storage/blob/44d007b4aded496edcb307e18c9be61ed6b25bbb/MA/Landing.png?raw=true)

## Client Page
The client page consists of a login page that takes registration and login details from the user. The details are then authenticated in the database.

Once the user logs in, they will enter the movie booking page. The movie booking page offers a variety of movies to choose from. The user can select and book a movie of their choice.

After the movie ticket is booked, the details of the person from the login are saved in a CSV file. This file is used to generate movie analytics.
- ### Login with registration/login details
    ![App Screenshot](https://github.com/prathameshparit/Dummy-Storage/blob/44d007b4aded496edcb307e18c9be61ed6b25bbb/MA/Login.png?raw=true)
- ### Authenticates user in database
- ### Movie booking page with various options
    ![App Screenshot](https://github.com/prathameshparit/Dummy-Storage/blob/44d007b4aded496edcb307e18c9be61ed6b25bbb/MA/Home.png?raw=true)
- ### Movies to book
    ![App Screenshot](https://github.com/prathameshparit/Dummy-Storage/blob/44d007b4aded496edcb307e18c9be61ed6b25bbb/MA/Movies.png?raw=true)
- ### Booked details saved in a CSV file
    ![App Screenshot](https://github.com/prathameshparit/Dummy-Storage/blob/44d007b4aded496edcb307e18c9be61ed6b25bbb/MA/Booked.png?raw=true)

## Admin Page
The admin page provides a dashboard with various interactive graphs and charts that display the movie analytics. The user can hover over the charts to see the details.
- ### Dashboard with interactive analytics charts
    ![App Screenshot](https://github.com/prathameshparit/Dummy-Storage/blob/44d007b4aded496edcb307e18c9be61ed6b25bbb/MA/Dashboard.png?raw=true)


- ### Hover to view details
    ![App Screenshot](https://github.com/prathameshparit/Dummy-Storage/blob/813d335ed2273efa798e11bdacf90ca01114a718/MA/Hover.png?raw=true)

- ### Ideal offer prediction using regression algorithms
    ![App Screenshot](https://github.com/prathameshparit/Dummy-Storage/blob/813d335ed2273efa798e11bdacf90ca01114a718/MA/Predict.png?raw=true)


- ### Algorithms
    ![App Screenshot](https://github.com/prathameshparit/Dummy-Storage/blob/44d007b4aded496edcb307e18c9be61ed6b25bbb/MA/Algos.png?raw=true)

    - Linear Regression
    - SVR
    - Decision Tree
    - Random Forest
    - Gradient Boosting
    - K-Nearest Neighbors
    - MLP

- ### Performance Parameters
    ![App Screenshot](https://github.com/prathameshparit/Dummy-Storage/blob/44d007b4aded496edcb307e18c9be61ed6b25bbb/MA/Metrics.png?raw=true)
    To evaluate the performance of our models, we used a range of performance parameters including:
    1. R-squared
    2. MAE
    3. MSE
    4. RMSE
- ### Comparative Analysis
    ![App Screenshot](https://github.com/prathameshparit/Dummy-Storage/blob/44d007b4aded496edcb307e18c9be61ed6b25bbb/MA/comparative.png?raw=true)




## Results
Movie Analytics is a comprehensive solution for movie booking and analysis. With its interactive charts and ideal offer prediction, it provides a complete solution for the movie industry.
This project provides a seamless solution for movie analytics, from booking to analytics and prediction.


## Tech

The website uses a number of open source projects to work properly:

- [Tensorflow] - Deep learning application framework
- [Scikit-Learn] - Bank for classification, predictive analytics, and very many other machine learning tasks.
- [Flask] - Framework for creating web applications in Python easier.
- [Matplotlib] - A low level graph plotting library in python that serves as a visualization utility.
- [Numpy] - Used for working with arrays
- [Pandas] - Used for data analysis and associated manipulation of tabular data in Dataframes


## Installation

Website requires these steps to install the application on your device


**On terminal:**

Download virtual env library
```sh
pip3 install -U pip virtualenv
```

Create a virtual environment on your device
```sh
virtualenv  -p python3 ./venv
```

Download all the dependencies provided on requirements.txt
```sh
pip install -r .\requirements.txt
```

Activated the virtual environment
```sh
.\pp\Scripts\activate
```

Run app.py after completing all the steps.





[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


[Tensorflow]: <https://www.tensorflow.org/>
[Scikit-Learn]: <https://scikit-learn.org/stable/>
[Flask]: <https://flask.palletsprojects.com/en/2.1.x/>
[Matplotlib]: <https://matplotlib.org/>
[Numpy]: <https://numpy.org/>
[Pandas]: <https://pandas.pydata.org/>
