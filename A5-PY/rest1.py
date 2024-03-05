import requests

# Define the base URL of the REST API endpoint
base_url = "https://jsonplaceholder.typicode.com/posts"

# Function to print response data


def print_response(response):
    print("Status Code:", response.status_code)
    print("Response Data:")
    print(response.json())


# Send a POST request to create a new post
new_post_data = {
    "title": "New Post",
    "body": "This is the body of the new post.",
    "userId": 1
}
response_post = requests.post(base_url, json=new_post_data)
print("\nCreating a new post:")
print_response(response_post)

# Send a PUT request to update an existing post
update_post_data = {
    "title": "Updated Post",
    "body": "This is the updated body of the post.",
    "userId": 1
}
response_put = requests.put(base_url + "/1", json=update_post_data)
print("\nUpdating an existing post:")
print_response(response_put)

# Send a DELETE request to delete a post
response_delete = requests.delete(base_url + "/1")
print("\nDeleting an existing post:")
print_response(response_delete)
