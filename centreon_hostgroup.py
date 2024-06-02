# Import modules
import requests
from dotenv import load_dotenv, find_dotenv, set_key
import os
import json

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


def cent_list_hg(domain = centreon_url, cent_api=api_token):
    base_url = f"{domain}action=action&object=centreon_clapi"
    headers = {"Content-Type": "application/json", "centreon-auth-token": f"{cent_api}"}

    body = {
        "action": "show",
        "object": "HG"
    }
    response = requests.post(base_url+clapi_url, json=body, headers=headers, verify=False)

    print(response.json())

    with open('centreongroups.json', 'w') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)

try:
    cent_list_hg()

except:
    cent_api()
    cent_list_hg()
