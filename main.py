from flask import Flask, request, jsonify
from flask_restful import Api, Resource

from sentient import sentient
from model import prediction
from data import rsi,call


# Create a Flask app
app = Flask(__name__)
api = Api((app))

# Define a route for accepting input data and returning predictions


@app.route('/predict', methods=['POST'])
def make_prediction():
    symbol = request.get_json()["symbol"]
    return jsonify(prediction(symbol))

@app.route('/sentient', methods=['POST'])
def make_sentient():
    symbol = request.get_json()["symbol"]
    vals = sentient(symbol)
    return jsonify(vals)

@app.route('/rsi', methods=['POST'])
def get_rsi():
    symbol = request.get_json()["symbol"]
    # iteration, price, gain, loss, avg_gain, avg_loss, rsi
    output = rsi(symbol)
    # print(output)
    return jsonify(output)

@app.route('/data', methods=['POST'])
def get_data():
    symbol = request.get_json()["symbol"]
    # iteration, price, gain, loss, avg_gain, avg_loss, rsi
    return jsonify(call(symbol))



# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
