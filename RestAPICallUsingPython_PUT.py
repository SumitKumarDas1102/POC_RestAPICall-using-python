import requests
import json

#Prepare POC how to call a Rest API PUT using python

#Call a PUT API and check the Respose of the API.
#PUT method using for update an existing record into the DB.

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
    "job": "zion resident"
}

#Hit the API
API_Response = requests.put(url= getURL, headers=headers, data= Request_Body)

# extracting data in json format 
Response_status = API_Response.status_code
Response_Body = API_Response.json()

print(Response_status)
print(Response_Body)