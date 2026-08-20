from bs4 import BeautifulSoup
import requests
import time

r = requests.get("https://www.croma.com/phones-wearables/mobile-phones/android-phones/c/95", timeout=10)
# print(dir(r))
# print(r.ok)
# print(r.status_code)
# print("fineeee")
# print(r.headers)
# r = r.text

soup = BeautifulSoup(r.text,"html.parser")
# soup.find("h1")
product = (soup.find_all(class_ = "product-item"))
# print(product)
# print(text.text)
for product in product:
    # print(heading.text)
    # print(soup.find("div"))
    
    # (soup.find(class_="plp-prod-title-rating-cont"))
    h3=(product.find("h3"))
    na=(h3.find('a'))
    print(na.text)
    # print(soup.find(class_="new-price plp-srp-new-price-cont"))
    
