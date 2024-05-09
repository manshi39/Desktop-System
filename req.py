import requests

# Define the URL of your desktop's Flask web server
desktop_url = "http://172.20.10.2:5000/unlock"  # Replace "your-desktop-ip" with your desktop's IP address

# Define the payload (data) to be sent with the request
payload = {'name': 'manshi'}  # Replace 'specific_name' with the name that unlocks your desktop

# Send a POST request to the desktop's Flask web server
try:
    response = requests.post(desktop_url, data=payload)
    if response.status_code == 200:
        print("Desktop unlocked successfully")
    else:
        print("Failed to unlock desktop - Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Failed to unlock desktop - Error:", e)
