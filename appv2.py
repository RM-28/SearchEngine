from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask_cors import CORS

import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()



app = Flask(__name__)
CORS(app)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/search', methods=['GET'])
def index():
    # Get the query parameter from the request
    query = request.args.get('q')


    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    
    #generate response from gemini
    results = model.generate_content(query)


    # Check if results were fetched successfully
    if results is None:
        return jsonify({"error": "Failed to fetch results"}), 500

    # Return the search results as a JSON response
    return jsonify(results.text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
