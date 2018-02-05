import requests

#实例1
url = 'https://item.jd.com/2967929.html'
url2 = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'

kv = {'user-agent': 'Mozilla/5.0'}
r = requests.get(url2, headers=kv)
# r = requests.get(url2)
print(r.status_code)
print(r.encoding)
# r.encoding = r.apparent_encoding
print(r.request.headers)
