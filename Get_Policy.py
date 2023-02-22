import json
from tetpyclient import RestClient

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Secure Workload
API_ENDPOINT="https://secure_workload.com"
searchFilter = "scope"
# Secure Workload API Auth
restclient = RestClient(API_ENDPOINT, credentials_file='credentials.json', verify=False)

# GET APP ID
resp=restclient.get('/applications')
json_resp = json.loads(resp.text)
json_formatted_str = json.dumps(json_resp, indent=2)
print(json_formatted_str)
app_id=json_resp[0]['id']
print("App_id:",app_id)

resp=restclient.get('/applications/'+app_id+'/policies')
json_resp = json.loads(resp.text)
json_formatted_str = json.dumps(json_resp, indent=2)
print(json_formatted_str)
