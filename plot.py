import warnings
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')


def comparative_plot(offer_DTR,
                        offer_GBR,
                        offer_KNR,
                        offer_LR,
                        offer_RFR,
                        offer_SVR):
    # model_columns is an empty list that will be used to create the DataFrame
    model_columns = []
    # model_compare is an empty Pandas DataFrame with no rows or columns
    model_compare = pd.DataFrame(columns=model_columns)
    # model_Name is a list of the names of the algorithms being compared
    model_Name = [
        'DTR',
        'GBR',
        'KNR',
        'LR',
        'RFR',
        'SVR'
    ]
    # accuracies is a list of the accuracies for each of the algorithms
    accuracies = [
        offer_DTR,
        offer_GBR,
        offer_KNR,
        offer_LR,
        offer_RFR,
        offer_SVR
    ]
    # Initialize counters for the loop
    count = 0
    row_index = 0
    # Iterate over the algorithm names and accuracies
    for i in model_Name:
        # model_name is the name of the current algorithm
        model_name = model_Name[count]
        # Add the algorithm name to the 'Name' column of the DataFrame
        model_compare.loc[row_index, 'Name'] = model_name
        # Add the accuracy to the 'Offer Predicted' column of the DataFrame
        model_compare.loc[row_index, 'Offer Predicted'] = accuracies[count]

        # Increment the counters
        count += 1
        row_index += 1

    # Sort the DataFrame by the 'Accuracies' column in descending order
    model_compare.sort_values(by=['Offer Predicted'], ascending=False, inplace=True)

    # Save the DataFrame as a CSV file
    model_compare.to_csv('static/assets/csv/compare.csv', encoding='utf-8-sig')

    # Create a bar plot of the algorithm accuracies using Seaborn
    plt.subplots(figsize=(15, 6))
    sns.barplot(x="Name", y="Offer Predicted", data=model_compare, palette='hot', edgecolor=sns.color_palette('dark', 7))
    plt.xticks(rotation=90)
    plt.title('Offer Predicted Comparison')
    # Save the plot as an image file
    plt.savefig('static/assets/img/model_compare.jpg')

    # Return the DataFrame
    return model_compare

#
# # Test
# offer_DTR, offer_GBR, offer_KNR, offer_LR, offer_RFR, offer_SVR = 0.5, 0.6, 0.7, 0.8, 0.9, 1.0
#
# comparative_plot(offer_DTR,
#                         offer_GBR,
#                         offer_KNR,
#                         offer_LR,
#                         offer_RFR,
#                         offer_SVR)
#
# import sklearn
# print(sklearn.__version__)