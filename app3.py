from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def process_query():
    data = request.json
    # Process the query here
    query = data.get('query')  # Assuming 'query' is the key for the text query
    # Your processing logic here
    response = {'processed_query': query}  # Dummy response for now
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

#chatgpt