# Import modules
import requests
from dotenv import load_dotenv, find_dotenv
import os

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

centreon_url = os.getenv('CENTREON_URL')
api_token = os.getenv('CENTREON_API')

base_url = f"https://{centreon_url}/centreon/api/index.php?"

clapi_url = "action=action&object=centreon_clapi"

headers = {"Content-Type": "application/json", "centreon-auth-token": f"{api_token}"}

body = {
    "action": "add",
    "object": "host",
    "values": "name;alias;ipaddress;hosttemplate;poller;hostgroup"
}

response = requests.post(base_url+clapi_url, json=body, headers=headers, verify=False)

print(response.json())