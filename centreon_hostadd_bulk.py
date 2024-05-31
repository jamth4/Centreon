# Import modules
import requests
from dotenv import load_dotenv, find_dotenv
import os
import csv

# Variables             
csv_path = '<path to file>'
dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

centreon_url = os.getenv('CENTREON_URL')
api_token = os.getenv('CENTREON_API')

base_url = f"https://{centreon_url}/centreon/api/index.php?"

clapi_url = "action=action&object=centreon_clapi"

headers = {"Content-Type": "application/json", "centreon-auth-token": f"{api_token}"}

# iterate through each line in the csv file and add the host info into to the API POST command
with open(csv_path, newline='') as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    next(file, None)
    for row in file:
        line = ';'.join(row)
        print(line)
        body = {
            "action": "add",
            "object": "host",
            "values": f"{line}"
        }
        response = requests.post(base_url+clapi_url, json=body, headers=headers, verify=False)