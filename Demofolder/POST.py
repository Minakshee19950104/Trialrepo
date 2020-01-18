#Need to install requests package for python
 #sudo easy_install requests
import requests
 
 # Set the request parameters
url = 'https://dev60544.service-now.com/api/now/table/incident'
user = 'admin'
pwd = 'Mina1234@'
 
 # Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}


 # Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers ,data='{"number":"INC1111111" , "short_description":"I am creating an incident for first time"}' )
 
 # Check for HTTP codes other than 200
if (response.status_code !=201):
                         print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
                         exit()
 
 # Decode the JSON response into a dictionary and use the data
 
print('Status:',response.status_code,'Headers:',response.headers,'Response:',response.json())

