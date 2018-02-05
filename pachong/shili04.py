import requests
from bs4 import BeautifulSoup

url = 'http://www.ip138.com/ips138.asp?ip='
r = requests.get(url + '202.204.80.112')
print(r.status_code)
r.encoding = r.raise_for_status()
print(len(r.text))
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
# print(soup.body.contents)
# list_a = []
# for child in soup.body.children:
#     list_a.append(child)
addr = soup.body.contents[9].li.string
print(addr[5:])
