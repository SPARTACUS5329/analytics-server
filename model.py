import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


from pandas_datareader.data import DataReader
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from datetime import datetime



def prediction(symbol):
    df = pdr.get_data_yahoo(symbol, start='2012-01-01', end=datetime.now())
    data = df.filter(['Close'])
    dataset = data.values
    training_data_len = int(np.ceil( len(dataset) * .95 ))

    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(dataset)

    model = tf.keras.models.load_model('main.h5')

    test_data = scaled_data[training_data_len - 60: , :]

    x_test = []
    for i in range(60, len(test_data)):
        x_test.append(test_data[i-60:i, 0])

    # Convert the data to a numpy array
    x_test = np.array(x_test)

    # Reshape the data
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1 ))

    # Get the models predicted price values 
    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)
    return({'predictions':list(predictions)})





