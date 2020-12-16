import requests
import json

#Prepare POC how to call a Rest API POST using python

#Call a POST API and check the Respose of the API.
#POST method using for create a new record into the DB.

#API URL / end point
getURL = "https://reqres.in/api/users"

#API headers
headers = {
            'Accept': '*/*',
            'Accept-Charset': 'utf-8'
              }

#API Request body / Request param
Request_Body = {
    "name": "morpheus",
    "job": "leader"
}

#Hit the API
API_Response = requests.post(url= getURL, headers=headers, data= Request_Body)

# extracting data in json format 
Response_status = API_Response.status_code
Response_Body = API_Response.json()

print(Response_status)
print(Response_Body)