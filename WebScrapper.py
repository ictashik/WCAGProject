from bs4 import BeautifulSoup
import urllib.request
import re

print('Sample Web Scrapper')

urlinput = input()


html_page = urllib.request.urlopen(urlinput)
soup = BeautifulSoup(html_page)
links = []

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    links.append(link.get('href'))

for a in range(len(links)):
    print(links[a])
