''' web scrapping
    beautifulsoup4 :tool for web scrapping
    pip install beautifulsoup4
    pip install requests
    allow to access html files

'''

#https://www.udemy.com/robots.txt

import requests
from datetime import time
from bs4 import BeautifulSoup
res=requests.get('https://news.ycombinator.com/news')
soup=BeautifulSoup(res.text,'html_parser')

print(soup.body.contents)
print(soup.findall('div'))
print(soup.findall('a'))
print(soup.title)
print(soup.find(id='score_20514755'))
print(soup.select('div')) #selectors
print(soup.select('.score')) #access using class name
print(soup.select('#score_20514755')) #access using id

