import requests
import time

headers = {
    'Authorization': 'Token 9nhSTk9cem2WQQXcOI3demVe',
}

# Read the data from the CSV file
with open('fubo_output_urls.csv', 'r') as file:
    # Skip the header row
    next(file)

    # Process each line in the CSV file
    for line in file:
        Channel, URL = line.strip().split(',')

        # Stop the stream
        stop_endpoint = f'http://dimobln.ddns.net:80/api/stream/{Channel}/stop'
        stop_response = requests.post(stop_endpoint, headers=headers)
        if stop_response.status_code == 200:
            print(f"Successfully stopped stream: {Channel}")
        else:
            print(f"Failed to stop stream: {Channel}")

        # Wait for 10 seconds
        time.sleep(10)

        # Start the stream
        start_endpoint = f'http://dimobln.ddns.net:80/api/stream/{Channel}/start'
        start_response = requests.post(start_endpoint, headers=headers)
        if start_response.status_code == 200:
            print(f"Successfully started stream: {Channel}")
        else:
            print(f"Failed to start stream: {Channel}")
