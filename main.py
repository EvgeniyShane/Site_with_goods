import json
from bs4 import BeautifulSoup
import requests

link = "https://www.sulpak.kz/f/smartfoniy"

page = requests.get(link)
soup = BeautifulSoup(page.text, "html.parser")

title = soup.find_all("div", class_="product__item-name")
if not title:
    raise Exception("The product names could not be found")

prices = soup.find_all("div", class_="product__item-price")
if not prices:
    raise Exception("The product prices could not be found")

result = []
for name, price in zip(title, prices):
    name_text = name.text.strip().replace("\n", "")
    price_text = price.text.strip().replace("\n", "")
    result.append({"title": name_text, "price": price_text})

with open("result.json", "w", encoding="utf-8") as json_file:
    json.dump(result, json_file, ensure_ascii=False)

print("Results saved to result.json")