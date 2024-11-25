import requests
import json
import pytest

@pytest.fixture(scope= "function")
def get_response():

    url = "https://gorest.co.in/public/v2/users/"
    headers = {"content_type": "application/json", "authorization":'Bearer e9f88597d84fadf0e4a7670bd20c7543435179b3f7268e7394968a103639a96b' }
    params ={}
    response =  requests.get(url, json.dumps(params), headers =  headers)
    # content = response.content
    # names = i.get("name")
    # print(json.loads(content))
    names=[]
    print(response.json)
    for i in response.json():
       names.append(i.get("name"))
    return names

def post_response():

    url = "https://gorest.co.in/public/v2/users"
    headers = {"content_type": "application/json", "authorization":'Bearer e9f88597d84fadf0e4a7670bd20c7543435179b3f7268e7394968a103639a96b' }
    payload ={ 'name': 'Linda', 'email': 'linda@15ce.com', 'gender': 'female', 'status': 'active'}
    response =  requests.post(url, data = payload, headers =  headers)
    print(response.json())


def patch_response():
    url = "https://gorest.co.in/public/v2/users/314"
    headers = {"content_type": "application/json",
               "authorization": 'Bearer e9f88597d84fadf0e4a7670bd20c7543435179b3f7268e7394968a103639a96b'}
    payload = {'name': 'Linda Catherine'}
    response = requests.patch(url, data=payload, headers=headers)
    print(response.json())


@pytest.mark.parametrize("input", [("Linda")])
def test_get_response(input, get_response):
    print(get_response)
    assert input in get_response, "test failed"

patch_response()


