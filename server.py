from flask import Flask, request, jsonify

from main import process1, process2


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome'})

# TODO: Create a flask app with two routes, one for each function.
# The route should get the data from the request, call the function, and return the result.

@app.route('/process1', methods=['POST'])
def route_function_one():
    data = request.json
    result = process1(data)
    return jsonify(result=result)

@app.route('/process2', methods=['POST'])
def route_function_two():
    data = request.json
    result = process2(data)
    return jsonify(result=result)