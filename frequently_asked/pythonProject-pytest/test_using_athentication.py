import requests
from requests.auth import HTTPBasicAuth
auth= HTTPBasicAuth('user', 'pass')
# auth = ('user', 'pass')
resp =  requests.get("https://httpbin.org/basic-auth/user/pass", auth = auth)
print(resp.text)

# Using an Authorization Token as Credentials
authorization = {'Authorization': 'abcde12345'}
resp = requests.get('https://httpbin.org/basic-auth/user/pass', headers = authorization )
print(resp.status_code)

# Authentication in Requests with HTTPDigestAuth
from requests.auth import HTTPDigestAuth
auth = HTTPDigestAuth('user','pass')
resp = requests.get ('https://httpbin.org/basic-auth/user/pass', auth = auth)
print(resp)

from requests_oauthlib import OAuth1

oauth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
              'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
print(requests.get('https://api.twitter.com/1.1/account/verify_credentials.json', auth=oauth))

from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
from requests_oauthlib import OAuth1