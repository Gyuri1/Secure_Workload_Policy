import json
import sys
from tetpyclient import RestClient

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if (len(sys.argv) != 2) :
    print(f"python {sys.argv[0]} policy.json")
    exit()

policy_filename= sys.argv[1]
print(f"Reading policy file:{policy_filename}")
policy_data=''
try:
    f = open(policy_filename)
    req_payload = json.load(f)
    f.close()
except FileNotFoundError:
    print("File {} does not exist".format(target_csv+policy_filename+'.json')) 
  

#Secure Workload
API_ENDPOINT="https://secure_workload.com"
searchFilter = "scope"
# Secure Workload API Auth
restclient = RestClient(API_ENDPOINT, credentials_file='credentials.json', verify=False)

# GET APP ID
resp=restclient.get('/applications')
json_resp = json.loads(resp.text)
json_formatted_str = json.dumps(json_resp, indent=2)
#print(json_formatted_str)
app_id=json_resp[0]['id']
#print("App_id:",app_id)

resp=restclient.post('/applications/'+app_id+'/policies', json_body=json.dumps(req_payload))

json_resp = json.loads(resp.text)
json_formatted_str = json.dumps(json_resp, indent=2)
print(json_formatted_str)
