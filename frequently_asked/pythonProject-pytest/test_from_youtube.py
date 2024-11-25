import requests
import json
# resp =requests.get("https://reqres.in/api/users/2")
# print(resp)
# assert resp.status_code == 200, "code is not matching"
# print(resp.text)
# print(resp.content)
# print(resp.json())
p = {"page": 2}
resp = requests.get("https://reqres.in/api/users",params=p)
# print(resp.url)
# print(resp.json())
assert resp.json()['data'][0]['email'] == "michael.lawson@reqres.in"

payload = {
    "name": "linda",
    "job": "test"
}
f = open("data.json", "r")
f=f.read()
resp_post = requests.post("https://reqres.in/api/users", data = json.loads(f))
create = resp_post.json()
print(create)
assert create['job'] == "automation", "failed"
print(resp_post.headers.get("Content-Type"))

###post 2 user
payload1 ={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
resp_post1 =  requests.post("https://reqres.in/api/register", data=payload1)
print(resp_post1.json()['token'])

##update - put
payload2 ={
    "name": "linda",

}
resp_put =  requests.put("https://reqres.in/api/users/2", data=payload2)
print(resp_put.json()["name"])

##delete
resp_delete = requests.delete("https://reqres.in/api/users/2")

resp_timeout = requests.get("https://httpbin.org/delay/5", timeout =10)
print(resp_timeout.status_code)

resp= requests.get("https://the-internet.herokuapp.com/basic_auth", auth=("admin", "admin"))
print(resp.status_code)

# r = requests.delete('https://httpbin.org/delete', data ={'key2':'value2'})
# print(r.content)
# r = requests.put('https://httpbin.org/put', data ={'key2':'value2'})
# print(r.content)
# r = requests.post('https://httpbin.org/post', data ={'key3':'value3'})
# print(r.content)

