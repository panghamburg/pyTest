import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
print(soup.title)
print(soup.a)
print(soup.a.attrs)
print(soup.a.attrs['class'])
print(soup.a.attrs['href'])
print(soup.a.string)
print(soup.a.prettify())
#搜索全部a标签
for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.find_all(['a', 'b']))
#查询所有标签
for tag in soup.find_all(True):
    print(tag.name)

for tag in soup.find_all(re.compile('b')):
    print(tag.name)
