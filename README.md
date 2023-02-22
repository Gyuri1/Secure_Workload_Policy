# Secure_Workload_Policy

Secure Workload Policy import-export examples. 


Please update:

1. credentials.json file  -> based on Your own API credentials
2. API_ENDPOINT variable  -> based on Your own Secure Workload FQDN or IP address
3. searchFilter variable  -> based on Your own scope 



# How to use:

`python Get_Policy.py >policy_out.json`

You can modify the policy_out.json file according to Your needs and save it into policy_in.json.

`python Post_Policy.py policy_in.json`

