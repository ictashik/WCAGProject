from bs4 import BeautifulSoup
import urllib.request
import re

html_page = urllib.request.urlopen("https://arstechnica.com")
soup = BeautifulSoup(html_page)
links = []

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    links.append(link.get('href'))

print(links)
