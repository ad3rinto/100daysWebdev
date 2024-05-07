import requests

from bs4 import BeautifulSoup

# import lxml

URL = "https://news.ycombinator.com/news"
response = (requests.get(URL))
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.prettify())

list_of_titles = soup.find_all('tr', class_="athing")
score_of_titles = soup.find_all('span', class_="score")

for title, score in zip(list_of_titles, score_of_titles):
    print(f"{title.text}\nlink is 'https://news.ycombinator.com'{title.find('a', class_='athing')}\nScore {score.text}")

# # Print the scores
# for title, score in zip(list_of_titles, score_of_titles):
#     print(title.find('a', class_="storylink").get("href"))

# list_of_titles = soup.findAll(class_="titleline")
# score_of_titles = soup.findAll(class_="score")
# for item in list_of_titles:
#     title = (item.getText())
#     link = item.find('a').get('href')
#     for anotherItem in score_of_titles:
#         score = anotherItem.getText()
#     print(score)

    # score = item[score_of_titles]
    # title = item[list_of_titles].getText()
    # link = item[list_of_titles].find("a").get("href")
    #
    # print(f'This article with title {title} has {score}, find link to article here - {link}')

# score_of_titles = soup.findAll(class_="score")
# for item in score_of_titles:
#     score = item.text
#     print(score)


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
