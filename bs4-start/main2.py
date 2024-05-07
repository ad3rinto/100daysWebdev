import requests

from bs4 import BeautifulSoup
# import lxml

URL = "https://news.ycombinator.com/"
response = (requests.get(URL))
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.prettify())

list_of_titles = soup.findAll(class_="titleline")
for item in list_of_titles:
    print(item)


# data = urllib.request.urlopen(URL)
# content = data.read()
#
# soup = BeautifulSoup(content, "html.parser")
# # print(soup.prettify())
# heading = soup.title.get_text()
# print(heading)
# all_a_tags = soup.select('.athing')
# # print(all_a_tags)
# for item in all_a_tags:
#     # print(item.get_text())
#     print(item.select(".titleline a"))


