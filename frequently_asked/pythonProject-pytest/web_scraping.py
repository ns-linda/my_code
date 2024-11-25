import requests
from bs4 import BeautifulSoup

url="http://www.google.com"
Resp = requests.get("url")
soup = BeautifulSoup(Resp.content, "html5lib")
soup.prettify()



