#Need to install requests package for python
 #sudo easy_install requests
import requests
def deleting():
    

 
 # Set the request parameters
 
    url ='https://dev60544.service-now.com/api/now/table/incident'
    user = 'admin'
    pwd = 'Mina1234@'
 
 # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers)

 # Do the HTTP request
    result = requests.delete(query='{'number': 'INC00234'}')

    
 
 # Check for HTTP codes other than 200
    if response.status_code != 204:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()
 
 # Decode the JSON response into a dictionary and use the data
        print('Status:',response.status_code,'Headers:',response.headers)

deleting()
