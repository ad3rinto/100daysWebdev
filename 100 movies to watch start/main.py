import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200611015421/https://www.empireonline.com/movies/features/best-tv-shows-ever-2/"

# Write your code below this line 👇

web_data = requests.get(URL)
content = web_data.text

soup = BeautifulSoup(content, "html.parser")

title = soup.find_all("h3")

# Create list of all titles
list_of_titles = [name.text for name in title]
# print(list_of_titles)


# Create list of image links
images = soup.find_all("img")
list_of_images = [image.get("src") for image in images]


for a,b in zip(list_of_titles, list_of_images):
    print(a, b.split("_")[1])