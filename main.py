from flask import Flask, request, jsonify
from flask_restful import Api, Resource


from sentient import sentient
# Create a Flask app
app = Flask(__name__)
api = Api((app))

# Define a route for accepting input data and returning predictions


@app.route('/predict', methods=['POST'])
def make_prediction():
    # # Get the input data from the request
    # input_data = request.get_json()

    # # Make predictions using the loaded model
    # predictions = predict(input_data)

    # # Return the predictions as JSON
    # return jsonify(predictions)
    return jsonify("Hello")


def sentient(""):


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
