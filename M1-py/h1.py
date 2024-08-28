from bs4 import BeautifulSoup
import json

# Example HTML content (replace this with your actual HTML content)
html_content = """
<html>
<head><title>Sample HTML</title></head>
<body>
<div class="container">
    <div class="title">Title 1</div>
    <div class="content">Content 1</div>
</div>
<div class="container">
    <div class="title">Title 2</div>
    <div class="content">Content 2</div>
</div>
</body>
</html>
"""

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements with class "container"
containers = soup.find_all('div', class_='container')

# List to store extracted data
data = []

# Iterate over containers
for container in containers:
    # Extract title and content
    title = container.find('div', class_='title').text.strip()
    content = container.find('div', class_='content').text.strip()

    # Append extracted data to the list
    data.append({'title': title, 'content': content})

# Convert data to JSON format
json_data = json.dumps(data, indent=4)

# Print JSON data
print(json_data)
