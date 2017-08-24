import requests
from bs4 import BeautifulSoup
url = 'https://www.iald.org/Designers?search'

r = requests.get(url)

html_content = r.text

soup = BeautifulSoup(html_content, 'lxml')

print soup.find_all('h2')[0:10]