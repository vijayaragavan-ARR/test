from flask import Flask, request, jsonify
from nltk.tokenize import RegexpTokenizer
import nltk

# Initialize Flask app
app = Flask(__name__)

# Download NLTK resources 
nltk.download('punkt')       # Download punkt tokenizer resource
nltk.download('averaged_perceptron_tagger')  # Download averaged_perceptron_tagger resource

# Define auxiliary verbs and POS tags to remove
auxiliary_verbs = {'be', 'am', 'is', 'are', 'was', 'were', 'been', 'being', 'have', 'has', 'had', 'do', 'does'}
tags_to_remove = {'MD', 'PUNCT'}

# Initialize RegexpTokenizer with a pattern to tokenize words while excluding punctuations
tokenizer = RegexpTokenizer(r'\w+')

# Define route for POST requests to '/'
@app.route('/', methods=['POST'])
def get_filtered_words():
    # Get input_string from the JSON payload of the POST request
    input_string = request.json.get('input_string')

    # Tokenize input_string and perform part-of-speech tagging
    words = tokenizer.tokenize(input_string)
    tagged_words = nltk.pos_tag(words)

    # Filter out words based on specified POS tags and auxiliary verbs
    filtered_words = [word for word, tag in tagged_words if tag not in tags_to_remove and word.casefold() not in auxiliary_verbs]

    # Return filtered words as JSON response
    return jsonify({'filtered_words': filtered_words})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
