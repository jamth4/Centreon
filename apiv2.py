import requests
from dotenv import load_dotenv, find_dotenv, set_key
import os
import json
'''
Script to manually create an APIv2 token for Centreon.
'''

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

username = os.getenv("CENTREON_USER")
password = os.getenv("CENTREON_PASSWORD")
centreon_url = os.getenv("")

def cent_api(domain = centreon_url, username = username, password = password):
    baseurl = f"{domain}login"
    todo = {
        "security": {
            "credentials": {
                "login": f"{username}",
                "password": f"{password}"
            }
        }
    }
    response = requests.post(baseurl, json=todo, verify=False)

    cent_token = response.json()

    cent_data = json.dumps(cent_token)
    cent_data = json.loads(cent_data)

    cent_key = cent_data['security']['token']

    set_key(dotenv_file, 'CENTREON_API2', cent_key)

cent_api()