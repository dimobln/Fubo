import time
import pychrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import threading
import queue
import csv

def log_writer():
    with open("fubo_logs.txt", "w") as log_file:  # Open the file in write mode ("w") at the beginning of each session
        pass  # This will clear the file

    while True:
        message = log_queue.get()
        if message is None:
            break

        with open("fubo_logs.txt", "a") as log_file:  # Open the file in append mode ("a")
            log_file.write(message + "\n")
            log_file.flush()

def output_on_start(**kwargs):
    url = kwargs.get("request", {}).get("url", "")
    message = f"URL: {url}"
    log_queue.put(message)

def output_on_end(**kwargs):
    pass

# Specify the path to the Chrome binary
chrome_binary_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Specify the path to the chromedriver executable
chromedriver_path = "/opt/homebrew/bin/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # Set the new headless mode introduced in Chrome version 96
options.add_argument("--remote-debugging-port=8000")

# Set the binary location in ChromeOptions
options.binary_location = chrome_binary_path

# Initialize the ChromeDriver service with the specified path
service = Service(executable_path=chromedriver_path)

# Initialize the webdriver instance using the service and options
driver = webdriver.Chrome(service=service, options=options)

dev_tools = pychrome.Browser(url="http://localhost:8000")
tab = dev_tools.list_tab()[0]
tab.start()

log_queue = queue.Queue()
log_thread = threading.Thread(target=log_writer)
log_thread.start()

# Website URL and login credentials
login_url = 'https://www.fubo.tv/signin'
username = 'parsag123@gmail.com'
password = 'tensoccher'

# Step 1: Load the login page and input login credentials
driver.get(login_url)
time.sleep(5)  # Give time for the page to load (adjust as needed)

# Find the username and password input fields and fill in the login credentials
username_input = driver.find_element(By.XPATH, '//input[@data-testid="sign-in-email-fld"]')
password_input = driver.find_element(By.XPATH, '//input[@data-testid="sign-in-password-fld"]')

username_input.send_keys(username)
password_input.send_keys(password)

# Step 2: Submit the login form
login_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sign-in-email-btn"]')   # Use By.CSS_SELECTOR to locate elements
login_button.click()
time.sleep(7) # Give time for the page to load (adjust as needed)

# Step 3: Navigate to the "My Profile" element
logo_element = driver.find_element(By.XPATH, '//div[@class="profile-name"]')
logo_element.click()  # Click on the logo element
time.sleep(5) # Give time for the page to load (adjust as needed)

#-------------- ESPN ---------------

# Step 4: Open the "Guide" element
subpage_url = 'https://www.fubo.tv/watch?channelId=10179'  # Replace with the desired subpage URL
driver.get(subpage_url)

# Step 5: Monitor the network traffic on the subpage for a specified duration
duration = 5  # Duration to capture network traffic in seconds
start_time = time.time()

while time.time() - start_time < duration:
    start = time.time()

    tab.call_method("Network.enable", _timeout=20)
    tab.set_listener("Network.requestWillBeSent", output_on_start)
    tab.set_listener("Network.responseReceived", output_on_end)

    # Capture the time taken for the actions and print it (optional)
    log_queue.put(f"{int(time.time() - start)}")

    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # Move the mouse cursor by a small offset (you can adjust the offset values)
    actions.move_by_offset(5, 5).perform()
    time.sleep(10)  # Give time for the page to load (adjust as needed)

#-------------- ESPN 2 ---------------

# Step 6: Open the "Guide" element
subpage_url = 'https://www.fubo.tv/watch?channelId=12444'  # Replace with the desired subpage URL
driver.get(subpage_url)

# Step 7: Monitor the network traffic on the subpage for a specified duration
duration = 5  # Duration to capture network traffic in seconds
start_time = time.time()

while time.time() - start_time < duration:
    start = time.time()

    tab.call_method("Network.enable", _timeout=20)
    tab.set_listener("Network.requestWillBeSent", output_on_start)
    tab.set_listener("Network.responseReceived", output_on_end)

    # Capture the time taken for the actions and print it (optional)
    log_queue.put(f"{int(time.time() - start)}")

    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # Move the mouse cursor by a small offset (you can adjust the offset values)
    actions.move_by_offset(5, 5).perform()
    time.sleep(10)  # Give time for the page to load (adjust as needed)

#-------------- FS1 ---------------

# Step 8: Open the "Guide" element
subpage_url = 'https://www.fubo.tv/watch?channelId=94653'  # Replace with the desired subpage URL
driver.get(subpage_url)

# Step 9: Monitor the network traffic on the subpage for a specified duration
duration = 5  # Duration to capture network traffic in seconds
start_time = time.time()

while time.time() - start_time < duration:
    start = time.time()

    tab.call_method("Network.enable", _timeout=20)
    tab.set_listener("Network.requestWillBeSent", output_on_start)
    tab.set_listener("Network.responseReceived", output_on_end)

    # Capture the time taken for the actions and print it (optional)
    log_queue.put(f"{int(time.time() - start)}")

    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # Move the mouse cursor by a small offset (you can adjust the offset values)
    actions.move_by_offset(5, 5).perform()
    time.sleep(10)  # Give time for the page to load (adjust as needed)

#-------------- FS2 ---------------

# Step 10: Open the "Guide" element
subpage_url = 'https://www.fubo.tv/watch?channelId=69553'  # Replace with the desired subpage URL
driver.get(subpage_url)

# Step 11: Monitor the network traffic on the subpage for a specified duration
duration = 5  # Duration to capture network traffic in seconds
start_time = time.time()

while time.time() - start_time < duration:
    start = time.time()

    tab.call_method("Network.enable", _timeout=20)
    tab.set_listener("Network.requestWillBeSent", output_on_start)
    tab.set_listener("Network.responseReceived", output_on_end)

    # Capture the time taken for the actions and print it (optional)
    log_queue.put(f"{int(time.time() - start)}")

    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # Move the mouse cursor by a small offset (you can adjust the offset values)
    actions.move_by_offset(5, 5).perform()
    time.sleep(10)  # Give time for the page to load (adjust as needed)

#-------------- MSNBC ---------------

# Step 12: Open the "Guide" element
subpage_url = 'https://www.fubo.tv/watch?channelId=75083'  # Replace with the desired subpage URL
driver.get(subpage_url)

# Step 13: Monitor the network traffic on the subpage for a specified duration
duration = 5  # Duration to capture network traffic in seconds
start_time = time.time()

while time.time() - start_time < duration:
    start = time.time()

    tab.call_method("Network.enable", _timeout=20)
    tab.set_listener("Network.requestWillBeSent", output_on_start)
    tab.set_listener("Network.responseReceived", output_on_end)

    # Capture the time taken for the actions and print it (optional)
    log_queue.put(f"{int(time.time() - start)}")

    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # Move the mouse cursor by a small offset (you can adjust the offset values)
    actions.move_by_offset(5, 5).perform()
    time.sleep(10)  # Give time for the page to load (adjust as needed)

#-------------- beIN SPORTS ---------------

# Step 14: Open the "Guide" element
subpage_url = 'https://www.fubo.tv/watch?channelId=88749'  # Replace with the desired subpage URL
driver.get(subpage_url)

# Step 15: Monitor the network traffic on the subpage for a specified duration
duration = 5  # Duration to capture network traffic in seconds
start_time = time.time()

while time.time() - start_time < duration:
    start = time.time()

    tab.call_method("Network.enable", _timeout=20)
    tab.set_listener("Network.requestWillBeSent", output_on_start)
    tab.set_listener("Network.responseReceived", output_on_end)

    # Capture the time taken for the actions and print it (optional)
    log_queue.put(f"{int(time.time() - start)}")

    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # Move the mouse cursor by a small offset (you can adjust the offset values)
    actions.move_by_offset(5, 5).perform()
    time.sleep(10)  # Give time for the page to load (adjust as needed)

#-------------- beIN SPORTS En Español ---------------

# Step 16: Open the "Guide" element
subpage_url = 'https://www.fubo.tv/watch?channelId=88754'  # Replace with the desired subpage URL
driver.get(subpage_url)

# Step 17: Monitor the network traffic on the subpage for a specified duration
duration = 5  # Duration to capture network traffic in seconds
start_time = time.time()

while time.time() - start_time < duration:
    start = time.time()

    tab.call_method("Network.enable", _timeout=20)
    tab.set_listener("Network.requestWillBeSent", output_on_start)
    tab.set_listener("Network.responseReceived", output_on_end)

    # Capture the time taken for the actions and print it (optional)
    log_queue.put(f"{int(time.time() - start)}")

    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # Move the mouse cursor by a small offset (you can adjust the offset values)
    actions.move_by_offset(5, 5).perform()
    time.sleep(10)  # Give time for the page to load (adjust as needed)

#-------------- ESPNEWS ---------------

# Step 18: Open the "Guide" element
subpage_url = 'https://www.fubo.tv/watch?channelId=16485'  # Replace with the desired subpage URL
driver.get(subpage_url)

# Step 19: Monitor the network traffic on the subpage for a specified duration
duration = 5  # Duration to capture network traffic in seconds
start_time = time.time()

while time.time() - start_time < duration:
    start = time.time()

    tab.call_method("Network.enable", _timeout=20)
    tab.set_listener("Network.requestWillBeSent", output_on_start)
    tab.set_listener("Network.responseReceived", output_on_end)

    # Capture the time taken for the actions and print it (optional)
    log_queue.put(f"{int(time.time() - start)}")

    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # Move the mouse cursor by a small offset (you can adjust the offset values)
    actions.move_by_offset(5, 5).perform()
    time.sleep(10)  # Give time for the page to load (adjust as needed)

#-------------- Los Angeles Dodgers ---------------

# Step 20: Open the "Guide" element
subpage_url = 'https://www.fubo.tv/watch?channelId=18220'  # Replace with the desired subpage URL
driver.get(subpage_url)

# Step 21: Monitor the network traffic on the subpage for a specified duration
duration = 5  # Duration to capture network traffic in seconds
start_time = time.time()

while time.time() - start_time < duration:
    start = time.time()

    tab.call_method("Network.enable", _timeout=20)
    tab.set_listener("Network.requestWillBeSent", output_on_start)
    tab.set_listener("Network.responseReceived", output_on_end)

    # Capture the time taken for the actions and print it (optional)
    log_queue.put(f"{int(time.time() - start)}")

    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # Move the mouse cursor by a small offset (you can adjust the offset values)
    actions.move_by_offset(5, 5).perform()
    time.sleep(10)  # Give time for the page to load (adjust as needed)

#-------------- TUDN ---------------

# Step 22: Open the "Guide" element
subpage_url = 'https://www.fubo.tv/watch?channelId=88839'  # Replace with the desired subpage URL
driver.get(subpage_url)

# Step 23: Monitor the network traffic on the subpage for a specified duration
duration = 5  # Duration to capture network traffic in seconds
start_time = time.time()

while time.time() - start_time < duration:
    start = time.time()

    tab.call_method("Network.enable", _timeout=20)
    tab.set_listener("Network.requestWillBeSent", output_on_start)
    tab.set_listener("Network.responseReceived", output_on_end)

    # Capture the time taken for the actions and print it (optional)
    log_queue.put(f"{int(time.time() - start)}")

    # Create an instance of ActionChains
    actions = ActionChains(driver)

    # Move the mouse cursor by a small offset (you can adjust the offset values)
    actions.move_by_offset(5, 5).perform()
    time.sleep(10)  # Give time for the page to load (adjust as needed)

# Stop capturing network traffic and finish the log writer thread
log_queue.put(None)  # Signal the log_writer thread to exit
log_thread.join()    # Wait for the log_writer thread to finish

# Function to check if the URL contains "master.mpd" or "master.m3u8"
def has_master(url):
    return "master.mpd" in url or "master.m3u8" in url

# Set to keep track of callsigns written to the CSV
existing_callsigns = set()

# Define a dictionary to map channels to their decryption keys
decryption_keys = {}

# Read the decryption keys from the fubo_output_keyurls.csv file
with open("fubo_output_keyurls.csv", "r", newline="", encoding="utf-8") as key_file:
    csv_reader = csv.DictReader(key_file)
    for row in csv_reader:
        channel = row["Channel"].strip()
        key = row["Key"].strip()
        decryption_keys[channel] = key

# Set to keep track of callsigns written to the CSV
existing_callsigns = set()

# Define a list to store the channels and their corresponding URLs
found_channels_urls = []

# Step 9: Write the captured URLs to a CSV file with additional columns
with open("fubo_output_urls.csv", "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Channel", "URL"])  # Write the header row with column names

    with open("fubo_logs.txt", "r") as log_file:
        current_callsign = None

        for line in log_file:
            if "URL:" in line:
                url = line.replace("URL: ", "").strip()

                # Extract the callsign from the URL
                callsign_pos = url.find("callsign=")
                if callsign_pos != -1:
                    callsign_end_pos = url.find("&", callsign_pos)
                    callsign = url[callsign_pos + len("callsign="):callsign_end_pos]

                    # Check if the URL contains "master.mpd" or "master.m3u8" and %7Eexp%
                    if has_master(url) and "~st" in url:
                        # Check if the callsign has already been written to the CSV
                        if callsign not in existing_callsigns:
                            # Check if the channel requires a decryption key and append it
                            decryption_key = decryption_keys.get(callsign, "")
                            if decryption_key:
                                url += f"&decryption_key={decryption_key}"

                            # Write the row with the callsign and URL
                            csv_writer.writerow([callsign, url])
                            existing_callsigns.add(callsign)

                            # Store the channel and URL in the found_channels_urls list
                            found_channels_urls.append((callsign, url))

# Close the browser at the end of the script
try:
    tab.stop()
    dev_tools.close_tab(tab)
    dev_tools.close()
except Exception as e:
    # Handle the exception (you can log the error if needed)
    pass

# Add a short delay before quitting the driver
time.sleep(2)
driver.quit()

# Print out the found channels and their URLs
print("Channels and URLs found:")
for channel, url in found_channels_urls:
    print(f"Channel: {channel}, URL: {url}")
