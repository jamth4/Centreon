# Import modules
import requests
from dotenv import load_dotenv, find_dotenv, set_key
import os

# Set variables and pull account info

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

username = os.getenv("CENTREON_USER")
password = os.getenv("CENTREON_PASSWORD")
centreon_url = os.getenv('CENTREON_URL')

base_url = f"https://{centreon_url}/centreon/api/index.php?"
auth_url = "action=authenticate"
todo = {"username":f"{username}", "password": f"{password}"}

response = requests.post(base_url+auth_url, data=todo, verify=False)

cent_token = response.json()

print(cent_token)

cent_key = cent_token['authToken']

set_key(dotenv_file, 'CENTREON_API', cent_key)
