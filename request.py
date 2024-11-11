from flask import Flask, request, jsonify
from duckduckgo_search import DDGS
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['GET'])
def index():
    # Get the query parameter from the request
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400

    # Use DuckDuckGo to get search results
    results = DDGS().text(query, max_results=10)  # Adjust max_results as needed

    # Check if results were fetched successfully
    if results is None:
        return jsonify({"error": "Failed to fetch results"}), 500

    # Return the search results as a JSON response
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)