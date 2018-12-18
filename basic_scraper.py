

## Lets dig into some python!


## I have added notes to help us learn what is going on in this file
## While using python you can use additional "packages" to help enhance 
## the functionality of what you are trying to do. Here we are using 2 packages
## they are called requests (shown with the import requests statement) and 
## BeautifulSoup (shown with the from bs4 import BeautifulSoup statement). 
## We imported the entire requests package by saying import vs only importing a portion
## of the BeautifulSoup package by saying from bs4 import BeautifulSoup.

import csv
import requests
from bs4 import BeautifulSoup

## In python you define or set a variable by saying variable name = 4. 
## If we had titled our variable above number, if we asked python what number is
## it would tell us 4. So below we have set a variable called url which is the website
## page we would like to scrape for designers. It is important to remember to enclose this
## website page with '' or "". There is no difference. Pick one and stick with it. 

url = 'https://www.iald.org/Designers?search'

## Now we are going to use the requests package we imported above (on line 9). To do this,
## we define a variable, r, and define r as telling the requests package we want to get the 
## contents of the variable, url. And as you know we defined url above! 

r = requests.get(url)

## Now that we have defined r we can "call" it. This is a fancy term for make r run or turn on.
## Next we are setting a new variable called html_content equal to r.text. 
## You might ask why we defined r above and now are calling r.text. 
## We add .text to the variable in order to get all of the contents of the webpage in text form. 

html_content = r.text

## Below we use the BeautifulSoup package we imported on line 10. The package sets the syntax of 
## how to use it so know the first action (html_content) is reserved for whatever variable you stored
## the text of the website page you want to scrape in. The second action ('lxml') is determining
## which "parser" your code is going to use. This is more of an advanced feature but using this 
## parser ensures our code runs as fast as possible. Here we set soup = our BeatifulSoup function
## so we can call it further down into our code. 

soup = BeautifulSoup(html_content, 'lxml')

## The last thing we do is we want to print out what we scraped so we can see if it worked. To do this
## we use the convenient python function print. You can try this in your terminal by typing python
## this opens the interpreter (what makes your code run....don't worry about this definition) and then type
## print "hello world". You will see the interpreter respond with hello world. In this example,
## you told python to print out the words hello world, and it did it! We use beautifulsoups function
## find_all to find every instance of an h2 tag in the html (where our designers names are stored in the page)
## and then we ask python to print out the first 11 instances it found. This might seem a tad odd 
## as the code says 0:10, not 0:11. Python counts the first object in a list as 0. So if you ask 
## it to print out 0:10 it will actually return 11 examples! Minor detail but something to know. 

print soup.find_all('h2')[0:10]
print soup.find_all('a')[0:10]

## There is a lot you can do in addition to this. I have attached some other files in this repo 
## that show you some other examples. You can remove the html tags to just return names or you can save
## the list to a spreasheet. To keep things simple for this quick intro I didn't go that far. 
## I would be happy to do that for another lesson! 

## Hopefully this is helpful.
