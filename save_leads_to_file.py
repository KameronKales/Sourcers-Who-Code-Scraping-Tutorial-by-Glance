## This example will show you how to scrape a website, remove the html elements like <body> from the 
## scraped content and put all of the leads you scraped into one list together. 

## importing the same libraries as before. requests lets us grab the url and beautifulsoup4 
## does all of the hard work for grabbing the content on the url. 

## we now import csv so we can save our leads to a csv file. 

import requests 
from bs4 import BeautifulSoup
import csv

## here we are writing a for loop. This loop lets us iterate through the 89 different pages 
## of this website and grab all of the contact information, without manually clicking "next page"
## each time. You don't really need to understand why this works. Just fill in the number where 1 is 
## currently with how many pages you need to iterate through. Add one to the total, so if you want to
## iterate through 2 pages, put 3 in the ().
for i in range(3): 
## Next we build our URL to scrape. We are doing a little bit of magic here to fill in the number from
## above. The purple bracket is being passed in our number from line 15 (1, 2, 3, etc). So this code 
## effectively loads a seperate request for each page we ask it to grab. In our case, it would be 90
## if we wanted to scrape the entire website. 
    url = "https://www.iald.org/Designers?search&page={}".format(i)
## Here we are setting up our request by passing the request library our url, and the headers needed 
## to fool the website into thinking we are a human. This is another one of those things you don't really 
## need to understand why it works. Just use the same syntax for your example and it will work. 
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'})
## here we define soup as our beautifulsoup element and limit the request to just the text by saying r.text.
## The 'lxml' is another don't worry about what this means portion. Just include it in your code like I have done
## and it will run exponentially faster than it will without. 
    soup = BeautifulSoup(r.text, 'lxml')

## Here we initialize an empty list called leads. We have to do this outside of our next for loop.
leads = []
## This for loop finds all of the elements that are enclosed in h2 tags and appends them into the
## leads list. Appending add each element into the list without replacing any of the other elements.
for sub_heading in soup.find_all('h2'):
    lead = sub_heading.text.encode('utf-8')
    leads.append(lead)
    print lead

## Now we will save this list to a csv file.
   
with open("leads.csv", "wb") as f:
    writer = csv.writer(f, delimiter=' ',
                            escapechar=' ', quoting=csv.QUOTE_NONE)
    writer.writerow(leads)


