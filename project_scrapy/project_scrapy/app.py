from flask import Flask, request, jsonify
import main as main

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def process_query():
    top_k = 10 # Get top 10
    data = request.json
    query = data.get('query')  # Assuming 'query' is the key for the text query
    result = main.query_return(query, top_k)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

#chatgpt