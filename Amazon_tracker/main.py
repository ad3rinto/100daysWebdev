import requests
from bs4 import BeautifulSoup
import lxml

# URL
URL = "https://www.amazon.co.uk/Holy-Stone-Quadcopter-Altitude-Beginners/dp/B07VJNG56X?ref_=ast_sto_dp"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

# Get the webpage
response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("£")[1]
# print(price_without_currency)
price_as_float = float(price_without_currency)
print(price_as_float)
