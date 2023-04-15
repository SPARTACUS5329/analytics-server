import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Define a function that takes input data and returns predictions


def predict(input_data):
    # Convert input data to numpy array
    input_array = np.array(input_data).reshape(1, -1)

    # Make predictions using the loaded model
    predictions = model.predict(input_array)

    # Convert predictions to a list and return
    return predictions.tolist()
