import requests
from bs4 import BeautifulSoup


r= requests.get('https://www.geeksforgeeks.org/python-programming-language/')
soup = BeautifulSoup(r.content, "lxml")
print(soup)
