from bs4 import BeautifulSoup
import pprint
import requests

r = requests.get('https://www.kslaw.com/people')
soup = BeautifulSoup(r.text, 'html.parser')
#print type(soup)
print soup.prettify()[0:1000]
'''
people = soup.find_all(class_="person")

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(people)
'''