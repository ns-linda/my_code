import pytest
import requests
import json

@pytest.fixture()
def test_callapi():
        global names
        consolidated_reult = {}
        endpoint="https://gorest.co.in/public/v2/users"
        method= "GET"
        headers = {'content_type': 'application/json', 'Accept': 'text/plain',
                'Authorization': 'Bearer e9f88597d84fadf0e4a7670bd20c7543435179b3f7268e7394968a103639a96b'
                }
        if method == "POST":
            content = requests.post(endpoint,headers= headers)
            print(content.content)
            resp = content.content

        elif method == "GET":
            content = requests.get(endpoint,headers= headers)
            resp = content.content
            consolidated_result = json.loads(resp.decode('UTF-8'))
            names = []
            for i in consolidated_result:
                names.append(i.get('name'))

        return names


@pytest.mark.parametrize('input',["Uday Sankar"])
def test_names(test_callapi, input):
        # print(get_names())
        assert input in test_callapi, "test failed"





