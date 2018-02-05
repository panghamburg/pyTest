import requests

"""
自动提交
百度 http://www.baidu.com/s?wd=xxx
360 http://www.so.com/s?q=xxx
"""
b_url = 'http://www.baidu.com/s'
s_kv = {'wd': '新闻'}
l_kv = {'user-agent': 'Mozilla/5.0'}
r = requests.get(b_url, headers=l_kv)
r = requests.get(b_url, params=s_kv)
print(r.status_code)
print(r.request.url)
print(len(r.text))

#范式的写法
def getHTMLTEXT(url):
    try:
        s_param = {'wd': '新闻'}
        r = requests.get(url, params=s_param)
        r.raise_for_status()
        return len(r.text)
    except:
        return 'error'


