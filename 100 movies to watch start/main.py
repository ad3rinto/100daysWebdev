import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200611015421/https://www.empireonline.com/movies/features/best-tv-shows-ever-2/"

# Write your code below this line 👇

web_data = requests.get(URL)
content = web_data.text

soup = BeautifulSoup(content, "html.parser")

title = soup.find_all("h3")

list_of_titles = [name.text for name in title]
print(list_of_titles)