import re

# Given list of dictionaries
data = [
    {'href': 'http://myhome.com', 'text': 'edited'},
    {'href': 'mailto:manipal@abcd.com', 'text': 'manipal@abcd.com'},
    {'href': 'mailto:manipal@xyz.com', 'text': 'manipal@xyz.com'},
    {'href': 'http://kinpin.com', 'text': 'pcgugt'}
]

# Regular expression pattern to match 'mailto:username@abcd.com'
pattern = r'mailto:(.*?)@abcd\.com'

# Extract the username from each dictionary in the list
usernames = []
for item in data:
    match = re.search(pattern, item.get('href', ''))
    if match:
        username = match.group(1)
        usernames.append(username)

print("Extracted usernames:", usernames)
