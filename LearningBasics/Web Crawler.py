import requests
from bs4 import BeautifulSoup


def book_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://books.toscrape.com/catalogue/category/books_1/page-" + str(page) + ".html"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.find_all("a"):
            title = str(link.get("title"))
            if title != "None":
                print(title)
        page += 1


book_spider(5)


