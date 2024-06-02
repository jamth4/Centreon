# Import modules
import requests
from dotenv import load_dotenv, find_dotenv, set_key
import os
import csv

csv_path = '<path to file>'
dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

username = os.getenv("CENTREON_USER")
password = os.getenv("CENTREON_PASSWORD")
centreon_url = os.getenv('CENTREON_URL')
api_token = os.getenv('CENTREON_API')

def cent_api (domain = centreon_url, username = username, password = password):
    '''Function to create api key if api authentication fails'''
    base_url = f"{domain}action=authenticate"
    todo = {"username":f"{username}", "password": f"{password}"}
    response = requests.post(base_url, data=todo, verify=False)

    cent_token = response.json()

    #print(cent_token)

    cent_key = cent_token['authToken']

    set_key(dotenv_file, 'CENTREON_API', cent_key) 


def cent_host_bulk(csv_path = csv_path, domain = centreon_url, api = api_token,):
    base_url = f"{domain}action=action&object=centreon_clapi"
    headers = {"Content-Type": "application/json", "centreon-auth-token": f"{api}"}

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
            response = requests.post(base_url, json=body, headers=headers, verify=False)

try:
    cent_host_bulk()

except:
    cent_api()
    cent_host_bulk()
