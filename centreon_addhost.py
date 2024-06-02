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

def add_host(values, domain=centreon_url,token=api_token):
    '''
    Function to manually add a host, values need to take the form:
    "name;alias;ipaddress;hosttemplate;poller;hostgroup"
    usage:
    add_host(values="pc1;pc1;10.10.10.10;OS-Linux-SSH-custom;central;Linux_Servers")
    '''
    clapi_url = f"{domain}action=action&object=centreon_clapi"
    headers = {"Content-Type": "application/json", "centreon-auth-token": f"{token}"}
    body = {
        "action": "add",
        "object": "host",
        "values": values
    }
    response = requests.post(clapi_url, json=body, headers=headers, verify=False)
    print(response.json())

try:
    add_host(values="pc1;pc1;10.10.10.10;OS-Linux-SSH-custom;central;Linux_Servers")
except:
    cent_api()
    add_host(values="pc1;pc1;10.10.10.10;OS-Linux-SSH-custom;central;Linux_Servers")
