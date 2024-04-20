import requests
import json

# Define the URL of your Flask server
url = 'http://localhost:5000/query'

# Define the JSON data to be sent in the request
user_query = input("Search: ")
json_data = {
    "query": user_query
}

# Send POST request with JSON data
response = requests.post(url, json=json_data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response from the server
    print("Response from server:")
    print(json.dumps(response.json(), indent=4))  # Pretty print the JSON response
else:
    print("Error:", response.status_code)
# Chat gpt