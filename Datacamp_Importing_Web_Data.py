from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup

url = "http://www.datacamp.com/teach/documentation"
request = Request(url)
response = urlopen(request)
html = response.read()
print(html)
response.close()

r = requests.get(url)
text = r.text
print(text)

url1 = 'https://www.python.org/~guido/'
r1 = requests.get(url1)
html_doc = r1.text
soup = BeautifulSoup(html_doc)
pretty_soup = soup.prettify()
print(pretty_soup)
guido_title = soup.Title
print(guido_title)
guido_text = soup.get_text()
print(guido_text)
a_tags = soup.find_all('a')
for link in a_tags:
    print(link.get('href'))
