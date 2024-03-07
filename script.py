import os
import requests
import hashlib

# Get the data from the URL
import os
import requests
import hashlib

SCRAPE_URL = os.environ.get('SCRAPE_URL', 'http://localhost:5000/data')

try:
    response = requests.get(SCRAPE_URL)
    data = response.json()
    samples = data['samples']
except requests.exceptions.RequestException as e:
    print(f"An error occurred while making the request: {e}")
    samples = []
except KeyError:
    print("The 'samples' key was not found in the response data.")
    samples = []


if not os.path.exists('files'):
    os.makedirs('files')

for item in samples:
    id = item['id']
    name = item['name']

    # Verify the SHA256 sum of the name matches the id
    sha256 = hashlib.sha256(name.encode()).hexdigest()
    if sha256 != id:
        print(f"SHA256 sum of name does not match id for item {id}. Skipping this!")
        continue
    else:
        print(f"SHA256 sum of name matches id for item {id}. Writing to file...")

    # Write the name to a file in the files directory
    with open(f"files/{id}.txt", 'w') as file:
        file.write(name)
