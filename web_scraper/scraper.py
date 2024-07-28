import requests
from bs4 import BeautifulSoup

url = "https://pixelford.com/blog"
response = requests.get(url, headers = {'user-agent': 'Usman-learns'})
html = response.content
soup = BeautifulSoup(html, 'html.parser')
a_tags = soup.find_all('a', class_="entry-title-link")


# for a_tag in a_tags:
#     print(a_tag.get_text())

titles = list(map(lambda a_tag: a_tag.get_text(), a_tags))

print(titles)