import requests
from bs4 import BeautifulSoup

# URL
URL = "https://news.ycombinator.com/news"

# Get the webpage
response = requests.get(URL)
yc_webpage = response.text

# Parse the HTML
soup = BeautifulSoup(yc_webpage, "html.parser")

# Find the titles and scores
list_of_titles = soup.find_all('tr', class_="athing")
score_of_titles = soup.find_all('span', class_="score")

# Print the titles, links, and scores
for title, score in zip(list_of_titles, score_of_titles):
    title_text = title.find('a', class_="storylink")
    link = "https://news.ycombinator.com/" + title.find('a', class_="storylink").get('href')
    print(f"Title: {title_text}")
    print(f"Link: {link}")
    print(f"Score: {score.text}")
    print("-" * 20)



# from bs4 import BeautifulSoup
# # import lxml
#
# with open("./website.html") as data:
#     content = data.read()
#     # print(content)
#
#
# soup = BeautifulSoup(content, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.text)
# # print(soup.prettify())
#
# all_a_tags = soup.findAll(name="a")
# # print(all_a_tags)
# # for anc in all_a_tags:
# #     print(anc.get("href"))
# #     print(anc.text)
# #     print(anc.getText())
# heading = soup.find(id="name").get_text()
# print(heading)
#
# heading2 = soup.find(name='h3', class_="heading").get_text()
# print(heading2)