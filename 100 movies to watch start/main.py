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
reversed_list = []

with open("series.txt","a") as file:
    for x in reversed(list_of_titles):
        file.write(x)
        file.write("\n")
    
    
# print(reversed_list)
# Create list of image links()
images = soup.find_all("img")
list_of_images = [image.get("src") for image in images]


# for a,b in zip(new_list_of_titles, list_of_images):
#     print(a)