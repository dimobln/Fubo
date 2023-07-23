import requests
import csv
import xml.etree.ElementTree as ET
import base64
import binascii

# Set your custom User-Agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

# Read the fubo_output_urls.csv file
with open('fubo_output_urls.csv', 'r', newline='') as file:
    csv_reader = csv.DictReader(file)
    channels = list(csv_reader)

# Create a list to store the results
results = []

# Process each channel
for channel_data in channels:
    channel_name = channel_data['Channel']
    url = channel_data['URL']

    # Send a GET request to the URL with the User-Agent header
    headers = {'User-Agent': USER_AGENT}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error retrieving data for Channel: {channel_name}")
        print(f"Status Code: {response.status_code}")
        print("---------------------")
        result = {
            'Channel': channel_name,
            'PSSH Values': 'Error retrieving data',
            'KID Values': 'Error retrieving data'
        }
        results.append(result)
        continue

    try:
        # Extract PSSH and KID from the manifest response
        manifest = response.text
        root = ET.fromstring(manifest)

        pssh_values = set()
        kid_values = set()
        for element in root.iter():
            if 'ContentProtection' in element.tag and 'urn:uuid:ede' in element.attrib.get('schemeIdUri', ''):
                pssh_element = element.find('cenc:pssh', {'cenc': 'urn:mpeg:cenc:2013'})
                if pssh_element is not None:
                    pssh_value = pssh_element.text.strip()
                    pssh_values.add(pssh_value)
                    try:
                        decoded_pssh = base64.b64decode(pssh_value)
                        if len(decoded_pssh) >= 36:
                            kid = binascii.hexlify(decoded_pssh[-16:]).decode()
                            kid_values.add(kid)
                    except binascii.Error:
                        pass

        if pssh_values or kid_values:
            print(f"Channel: {channel_name}")
            if pssh_values:
                print("PSSH Values:")
                for pssh_value in pssh_values:
                    print(pssh_value)
            if kid_values:
                print("KID Values:")
                for kid_value in kid_values:
                    print(kid_value)
            print("---------------------")

            result = {
                'Channel': channel_name,
                'PSSH Values': ', '.join(pssh_values),
                'KID Values': ', '.join(kid_values)
            }
        else:
            print(f"Channel: {channel_name}")
            print("No PSSH or KID found")
            print("---------------------")

            result = {
                'Channel': channel_name,
                'PSSH Values': 'No PSSH found',
                'KID Values': 'No KID found'
            }
    except Exception as e:
        print(f"Error processing data for Channel: {channel_name}")
        print(f"Error message: {str(e)}")
        print("---------------------")
        result = {
            'Channel': channel_name,
            'PSSH Values': 'Error processing data',
            'KID Values': 'Error processing data'
        }

    results.append(result)

# Save the results in a CSV file
filename = 'fubo_output_pssh_kid.csv'
fields = ['Channel', 'PSSH Values', 'KID Values']
with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(results)

print(f"PSSH and KID values saved in {filename}")
