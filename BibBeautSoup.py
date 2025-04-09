import requests
from bs4 import BeautifulSoup
from pprint import pprint


# url = "https://books.toscrape.com/"
# response =  requests.get(url)
#
# with open('index.html', 'w') as f :
#     html = f.write(response.text)

with open('index.html', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
aside = soup.find('div', class_="side_categories")
categories_div = aside.find("ul").find('li').find('ul')
categories = [child.text.strip() for child in categories_div.children if child.name]

images = soup.find('section').find_all('img')

sources = [image.get('src') for image in images]

pprint(sources)