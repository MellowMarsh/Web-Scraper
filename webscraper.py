import requests
from bs4 import BeautifulSoup

url = 'http://mothertreewellness.com'
response = requests.get(url, timeout = 5)
content = BeautifulSoup( response.content, "html.parser")

print (content)

