from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://www.investing.com"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
title = soup.title
print(title)
text = soup.get_text()
# print(text)
s = soup.find_all('a')
for link in s:
    print(link.get('href'))
rows = soup.find_all('tr')
for row in rows:
    row_td = row.find_all('td')
print(row_td)
