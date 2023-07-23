import requests

headers = {
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Authorization': 'Token 9nhSTk9cem2WQQXcOI3demVe',
}

# Read the data from the CSV file
with open('fubo_output_urls.csv', 'r') as file:
    # Skip the header row
    next(file)

    # Process each line in the CSV file
    for line in file:
        Channel, URL = line.strip().split(',')

        # Make the API request to update the URL for the current Channel
        json_data = [URL]
        response = requests.post(f'http://dimobln.ddns.net:80/api/stream/{Channel}/source-update', headers=headers, json=json_data)

        # Check the response status (optional)
        if response.status_code == 200:
            print(f"Successfully updated URL for {Channel}.")
        else:
            print(f"Failed to update URL for {Channel}. Status code: {response.status_code}")
