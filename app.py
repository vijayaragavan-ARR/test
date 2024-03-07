
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_words():
    # Get the input string from the request
    input_string = request.json.get('input_string')
    # Split the input string into words
    words = input_string.split()

    # Return the list of words as JSON
    return jsonify({'words': words})

if __name__ == '__main__':
    app.run(debug=True)
