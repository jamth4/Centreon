# Import modules
import requests
from dotenv import load_dotenv, find_dotenv
import os
import json

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

centreon_url = os.getenv('CENTREON_URL')
api_token = os.getenv('CENTREON_API')

base_url = f"https://{centreon_url}/centreon/api/index.php?"

clapi_url = "action=action&object=centreon_clapi"

headers = {"Content-Type": "application/json", "centreon-auth-token": f"{api_token}"}

body = {
    "action": "show",
    "object": "HG"
}

response = requests.post(base_url+clapi_url, json=body, headers=headers, verify=False)

print(response.json())

with open('centreongroups.json', 'w') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)