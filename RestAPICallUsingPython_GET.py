import requests
import json


#Prepare POC how to call a Rest API GET using python

#Call a GET API and check the Respose of the API. 
#GET - Method using for fetch any record from the DB. 

#API URL / end point
getURL = "https://reqres.in/api/users?page=2"

#API headers
headers = {
            'Accept': '*/*',
            'Accept-Charset': 'utf-8'
              }

#Hit the API
API_Response = requests.get(url= getURL, headers=headers)

# extracting data in json format 
Response_status = API_Response.status_code
Response_Body = API_Response.json()

#print the response
print(Response_status)
print(Response_Body)

