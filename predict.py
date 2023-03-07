# Importing libraries
import pickle
import sklearn

LR_model = pickle.load(open('models/LR.sav', 'rb'))
GBR_model = pickle.load(open('models/GBR.sav', 'rb'))
KNR_model = pickle.load(open('models/KNR.sav', 'rb'))
DTR_model = pickle.load(open('models/DTR.sav', 'rb'))
RFR_model = pickle.load(open('models/RFR.sav', 'rb'))
SVR_model = pickle.load(open('models/SVR.sav', 'rb'))

# Define the custom input
custom_input = [[100, 100]]


def predict_offer(custom_input):
    # Use the model to make a prediction
    predicted_offer_LR = LR_model.predict(custom_input)
    predicted_offer_GBR = GBR_model.predict(custom_input)
    predicted_offer_KNR = KNR_model.predict(custom_input)
    predicted_offer_DTR = DTR_model.predict(custom_input)
    predicted_offer_RFR = RFR_model.predict(custom_input)
    predicted_offer_SVR = SVR_model.predict(custom_input)

    # Print the prediction
    return round(predicted_offer_LR[0], 2), round(predicted_offer_GBR[0], 2), round(predicted_offer_KNR[0], 2), round(predicted_offer_DTR[0], 2), round(predicted_offer_RFR[0], 2), round(predicted_offer_SVR[0], 2)



