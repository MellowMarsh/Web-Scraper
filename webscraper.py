
import requests
from bs4 import BeautifulSoup
#pulling all homepage content to test out the web-scraper
url = 'http://mothertreewellness.com'
response = requests.get(url, timeout = 5)
content = BeautifulSoup( response.content, "html.parser")

print (content)
