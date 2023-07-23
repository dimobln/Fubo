import requests
import json
import csv

# API endpoint and URLs
api_url = "https://keysdb.net/api"
license_url = "https://irdeto.fubo.tv/licenseServer/widevine/v1/FuboTV/certificate"

# Retrieve channel names and PSSH values from the "fubo_output_pssh_kid.csv" file
channel_pssh_mapping = {}
with open('fubo_output_pssh_kid.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        channel_name = row['Channel']
        pssh_value = row['PSSH Values']
        channel_pssh_mapping[channel_name] = pssh_value

# Prepare the data for the new CSV file
data = []
for channel, pssh in channel_pssh_mapping.items():
    # Construct the payload with license_url and pssh
    payload = {
        "license_url": license_url,
        "pssh": pssh,
        "proxy": "",
        "buildinfo": "",
        "cache": True
    }

    # Headers with API key
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "X-API-Key": "c7c25d1a3ef991ecbf7465177dc6eb4b12a4b31d592485960627de2774284572"
    }

    # Send a POST request to the API
    response = requests.post(api_url, headers=headers, json=payload)
    api_response = response.text

    # Check if the response is valid JSON
    try:
        api_response = json.loads(api_response)
    except json.JSONDecodeError:
        print(f"Invalid JSON response for Channel: {channel}")
        continue

    # Extract the key value
    keys = api_response.get('keys')
    if keys:
        if isinstance(keys, list) and keys:
            key = keys[0].get('key')
            if isinstance(key, str):
                key_values = key.split(':')
                if len(key_values) == 2:
                    key = ':'.join(key_values)
                    print(f"Channel: {channel} | Key: {key}")
                    data.append({'Channel': channel, 'Key': key})
                else:
                    print(f"Invalid key format for Channel: {channel}")
            else:
                print(f"No key generated for Channel: {channel}")
        else:
            print(f"No key generated for Channel: {channel}")
    else:
        print(f"No key information in the response for Channel: {channel}")

# Save the data into a new CSV file
filename = 'fubo_output_keyurls.csv'
fields = ['Channel', 'Key']
with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

print(f"Data saved in {filename}")
