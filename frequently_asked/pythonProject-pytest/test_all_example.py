import requests
import pytest

@pytest.fixture(scope="class")
def prepare_input(request):
    request.cls.num = 10
    request.cls.num2 =15

@pytest.mark.usefixtures('prepare_input')
class Test_addition:
    def test_add(self):
        assert  add(self.num, self.num2) == 25, "test failed"

def add(num,num2):
    return num+num2


@pytest.fixture(scope="function")
def get_post():
    url = "https://gorest.co.in/public/v2/users/"
    header = {'authorization': 'Bearer e9f88597d84fadf0e4a7670bd20c7543435179b3f7268e7394968a103639a96b'}
    resp = requests.get(url, headers = header)
    nameslist=[]
    for names in resp.json():
        nameslist.append(names['name'])
    return nameslist

# @pytest.fixture(scope="function")
def patch():
    url = "https://gorest.co.in/public/v2/users/314"
    header = {'authorization': 'Bearer e9f88597d84fadf0e4a7670bd20c7543435179b3f7268e7394968a103639a96b'}
    data = { 'name': 'Linda', 'email': 'aditya@1345ce.com', 'gender': 'male', 'status': 'active'}
    resp = requests.patch(url, data = data, headers = header)
    # print(resp.json())
    # nameslist = []
    # for names in resp.json():
    #     nameslist.append(names['name'])
    # return nameslist

@pytest.mark.parametrize('input',['Aditya'])
def test_name(input, get_post):
    assert input in get_post, "test failed"

patch()


from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1

auth=OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

import json
f= open("data.json", 'r')
f=f.read()
resp = requests.post("https://reqres.in/api/users", data = json.loads(f))
f=open('data_output.json', 'w')
f.write(json.dumps(resp.json()))

