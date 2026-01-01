# product  data scraper

import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
}

url = "https://books.toscrape.com"
fl = []
n = 0
try:
    while True:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = "utf-8"
        soup = BeautifulSoup(r.text,"html.parser")
        items = soup.select("article.product_pod")

        for item in items:
            title = item.find("h3").find("a")
            book_title = title["title"]
            price = item.select_one("p.price_color").text
            avail = item.select_one("p.instock").get_text(strip=True)
            rating = item.select_one("p.star-rating")
            link = title["href"]
            book_link = urljoin(url,link)
            fl.append({
                "Book title":book_title,
                "Price":price,
                "Availability":avail,
                "Rating":rating["class"][-1],
                "Product page link": book_link
            })

        next = soup.select_one("li.next")

        if next is None:    
            break

        next_link = next.select_one("a")["href"]
        url = urljoin(url,next_link)
        print("Scraped page: ",n)
        n += 1
    ask = input("Save output as CSV or JSON? (csv/json): ").lower()


    if ask == "json":

        with open("Scraped_data.json","w",encoding="utf-8") as f:
            json.dump(fl ,f, indent=4, ensure_ascii=False)
            print("Scraping completed")
        
    elif ask == "csv":
        with open("Scraped_data.csv","w", newline= "", encoding="utf-8") as f:
            w = csv.DictWriter(f,fieldnames=["Book title","Price","Availability","Rating","Product page link"])
            w.writeheader()
            w.writerows(fl)


except requests.exceptions.RequestException as e:
    print(e)
