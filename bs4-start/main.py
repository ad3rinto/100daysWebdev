from bs4 import BeautifulSoup
# import lxml

with open("./website.html") as data:
    content = data.read()
    # print(content)


soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.text)
# print(soup.prettify())

all_a_tags = soup.findAll(name="a")
# print(all_a_tags)
# for anc in all_a_tags:
#     print(anc.get("href"))
#     print(anc.text)
#     print(anc.getText())
heading = soup.find(id="name").get_text()
print(heading)

heading2 = soup.find(name='h3', class_="heading").get_text()
print(heading2)