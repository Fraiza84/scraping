import requests
from bs4 import BeautifulSoup
from pprint import pprint


with open('index.html', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

#articles = soup.find_all('article' , class_= 'product_pod')

titles_tag = soup.find_all('a' , title = True)
titles = [ title.get('title') for title in titles_tag]

pprint(titles)