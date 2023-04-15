# Formula to calculate RSI
# RSI = 100 – (100 / [1 +RS ])

# Importing required packages

from datetime import datetime
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import yahoo_fin.stock_info as si

import numpy as np

def rsi(symbol):
    df = pdr.get_data_yahoo(symbol, start='2019-04-04', end=datetime.now())
    data = df.filter(['Close'])
    data = data.values

    window_length = 14

    # Initialize containers for avg. gains and losses
    gains = []
    losses = []

    # Create a container for current lookback prices
    window = []

    # Keeps track of previous average values
    prev_avg_gain = None
    prev_avg_loss = None

    # Create a container for our final output (as a csv)
    output = {'date':[], 'close':[], 'gain':[], 'loss':[], 'avg_gain':[], 'avg_loss':[], 'rsi':[]}

    for i, price in enumerate(data):
        if i == 0:
            window.append(price)
            output['date'].append(i+1)
            output['close'].append(price)
            output['gain'].append(0)
            output['loss'].append(0)
            output['avg_gain'].append(0)
            output['avg_loss'].append(0)
            output['rsi'].append(0)
            continue

        difference = np.round(data[i] - data[i - 1], 2)

        if difference > 0:
            gain = difference
            loss = 0

        elif difference < 0:
            gain = 0
            loss = abs(difference)

        else:
            gain = 0
            loss = 0

        gains.append(gain)
        losses.append(loss)

        if i < window_length:
            window.append(price)
            output['date'].append(i+1)
            output['close'].append(price)
            output['gain'].append(gain)
            output['loss'].append(loss)
            output['avg_gain'].append(0)
            output['avg_loss'].append(0)
            output['rsi'].append(0)
            continue
        if i == window_length:
            avg_gain = sum(gains) / len(gains)
            avg_loss = sum(losses) / len(losses)
        else:
            avg_gain = (prev_avg_gain * (window_length - 1) + gain) / window_length
            avg_loss = (prev_avg_loss * (window_length - 1) + loss) / window_length
        prev_avg_gain = avg_gain
        prev_avg_loss = avg_loss
        avg_gain = np.round(avg_gain, 2)
        avg_loss = np.round(avg_loss, 2)
        prev_avg_gain = np.round(prev_avg_gain, 2)
        prev_avg_loss = np.round(prev_avg_loss, 2)
        rs = np.round(avg_gain / avg_loss, 2)
        rsi = np.round(100 - (100 / (1 + rs)), 2)
        window.append(price)
        window.pop(0)
        gains.pop(0)
        losses.pop(0)
        output['date'].append(i+1)
        output['close'].append(price)
        output['gain'].append(gain)
        output['loss'].append(loss)
        output['avg_gain'].append(avg_gain)
        output['avg_loss'].append(avg_loss)
        output['rsi'].append(list(rsi))

    # iteration, price, gain, loss, avg_gain, avg_loss, rsi
    rsi = []
    for i in output['rsi']:
        if i.__class__ == list:
            rsi.append(i[0])
        else:
            rsi.append(i)
    return(rsi)


def call(symbol):
    msft_data = si.get_quote_table(symbol)
    return (msft_data)


    