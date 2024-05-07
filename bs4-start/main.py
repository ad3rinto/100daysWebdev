from bs4 import BeautifulSoup
# import lxml

with open("./website.html") as data:
    content = data.read()
    # print(content)


soup = BeautifulSoup(content, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.text)