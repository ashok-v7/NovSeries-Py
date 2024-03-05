import requests

# Define the URL of the REST API endpoint
api_url = "https://jsonplaceholder.typicode.com/posts"

# Send a GET request to the API endpoint
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response into a Python dictionary
    json_data = response.json()

    # Print the JSON data
    print("JSON Data:")
    print(json_data)

    # Extract information from JSON data
    for post in json_data:
        print("\nPost ID:", post["id"])
        print("Title:", post["title"])
        print("Body:", post["body"])

else:
    print("Failed to fetch data from the API. Status code:", response.status_code)


'''
Import the requests module to send HTTP requests to the API.
Define the URL of the REST API endpoint you want to interact with (api_url in this example).
Send a GET request to the API endpoint using requests.get().
Check if the request was successful (status code 200).
If the request was successful, parse the JSON response into a Python dictionary using .json() method.
Print the JSON data.
Extract information from the JSON data and process it as needed.
'''
