#Need to install requests package for python
 #sudo easy_install requests
import requests


 
 # Set the request parameters
url = 'https://dev60544.service-now.com/api/now/table/incident/21b704c7dbe90010bc4ce1bb4b96198e'
user = 'admin'
pwd = 'Mina1234@'
 
 # Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}
 
 # Do the HTTP request
response = requests.patch(url, auth=(user, pwd), headers=headers ,data='{"short_description":"not getting"}')
 
 # Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()
 
 # Decode the JSON response into a dictionary and use the data
print('Status:',response.status_code,'Headers:',response.headers,'Response:',response.json())

