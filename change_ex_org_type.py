import requests
import csv
import time

# Your API Key to Pure - needs to have read and write access to external organizations. Keep your key secure!
api_key = 'my_api_key'

# Base URL for the PUT requests - replace 'pure_instance_url' with the URL of your Pure
url = "https://pure_instance_url/ws/api/external-organizations/"

# Headers for the PUT requests
headers = {
    "accept": "application/json",
    "api-key": api_key,
    "Content-Type": "application/json"
}

# Data payload for the PUT requests. Change the uri to the type of external organisation you want to change the type to. In the classification scheme 'ueoexternalorganisationtypes' you will find the available uri's in your Pure. The uri below changes the type of the external orgs to "academic"
data = {
    "type": {
        "uri": "/dk/atira/pure/ueoexternalorganisation/ueoexternalorganisationtypes/ueoexternalorganisation/academic"
    }
}

# Function to send a PUT request to the Pure API
def send_put_request(uuid):
    response = requests.put(f"{url}{uuid}", headers=headers, json=data)
    if response.status_code == 200:
        print(f"Request to {uuid} was successful!")
    else:
        print(f"Request to {uuid} failed with status code {response.status_code}: {response.text}")

# Main function to read UUIDs from a CSV file and send PUT requests. Extract the UUID's of the external organisations you want to change the type on from Pure as csv format. Save in the same folder as this script. 
def main():
    with open('uuids.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            uuid = row.get('UUID')
            if uuid:
                send_put_request(uuid)
                time.sleep(1)  # Wait for one second between each request to go easy on the Pure API :-) 
            else:
                print("UUID not found in row")

# Entry point of the script
if __name__ == "__main__":
    main()
