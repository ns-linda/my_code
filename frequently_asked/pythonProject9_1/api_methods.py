import requests
import json


def get_response():

    url = "https://gorest.co.in/public/v2/users"
    headers = {"content_type": "application/json", "authorization":'Bearer e9f88597d84fadf0e4a7670bd20c7543435179b3f7268e7394968a103639a96b' }
    params ={}
    response =  requests.get(url, json.dumps(params), headers =  headers)
    print(response)
    content = response.content
    print(json.loads(content))
    for i in response.json():
        print(i.get("name"))

