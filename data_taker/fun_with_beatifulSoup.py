from bs4 import BeautifulSoup
import requests
from csv import writer

# response = requests.get('http://codedemos.com/sampleblog/')
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="https://pl.wikipedia.org/wiki/Babie_lato_(meteorologia)#/media/File:IndianSummer.jpg" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc, 'html.parser')


# find()
# el = soup.find_all(id='link1')
# el = soup.find(class_="story")
# el = soup.find(attrs={"data-hello": 'hi'})
# as list
# el = soup.select('.sister')
# el = soup.find(class_='sister').get_text()
# print(el)
# for item in soup.select('.sister'):
#     print(item.get_text())
# el = soup.body.contents[3].contents[1].find_next_sibling()
# el = soup.find(id='link2').find_previous_sibling()
# el = soup.find('a').find_parent()
# el = soup.find(class_="story").find_next_sibling('p')


# print(el)
