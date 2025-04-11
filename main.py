from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from pprint import pprint

BASE_URL = "https://books.toscrape.com"


def main(threshold: int=5 ):
    with requests.Session() as session:

        response = session.get(BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
       # soup.find("ul", class_= "nav nav-list").find_all("a")

        liens = soup.select('ul.nav.nav-list a')
        categories_url = [lien["href"] for lien in liens[1:]]

        for category_url in categories_url:
            full_url = urljoin(BASE_URL,category_url)
            response = session.get(full_url)
            soup = BeautifulSoup(response.text, "html.parser")
            books = soup.select("article.product_pod")
            category = soup.select_one("h1").text
            number_of_books = len(books)
            if number_of_books <= threshold:
                print(f"La catégorie {category} ne contient pas assez de livre ({len(books)})")

if __name__ == '__main__':
    main(threshold=10)

