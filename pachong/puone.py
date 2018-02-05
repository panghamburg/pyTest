import requests

#通用范式
def getHTMLTEXT(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '异常'

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(getHTMLTEXT(url))
