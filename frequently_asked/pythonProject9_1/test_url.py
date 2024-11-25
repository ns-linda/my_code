import unittest
import requests
import json

class test_call_api:

    def __init__(self):
        self.consolidated_reult = {}
        self.headers = {'content_type':'application/json', 'Accept': 'test/plain','Authorization': 'Bearer e9f88597d84fadf0e4a7670bd20c7543435179b3f7268e7394968a103639a96b'
        }


    def callapi(self, endpoint, method):
        if method == "POST":
            content = requests.post(endpoint,headers= self.headers)
            print(content.content)
            resp = content.content

        elif method == "GET":
            content = requests.get(endpoint,headers= self.headers)
            resp = content.content
            self.consolidated_result = json.loads(resp.decode('UTF-8'))
            # print(resp)

        return self.consolidated_result

    def get_names(self):

        data=self.callapi("https://gorest.co.in/public/v2/users", "GET")
        # print(data)
        names=[]
        for i in data:
            names.append(i.get('name'))

        return names

class SimpleTest(unittest.TestCase):
    def test_names(get_names):

        api = test_call_api()
        api.get_names()
        assert "Uday Sankar" in api.get_names(), "test failed"

if __name__ == '__main__':
    unittest.main()



