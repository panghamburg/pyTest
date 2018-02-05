import requests
import os
path = 'D:/Work/abc.jpg'
url = 'http://image.nationalgeographic.com.cn/2018/0201/20180201114431179.jpg'
# r = requests.get(url)
# print(r.status_code)
# with open(path, 'wb') as f:
#     f.write(r.content)
# f.close()

#范式写法
root = 'D:/Work/testPic/'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('已下载')
    else:
        print('已存在')
except:
    print('爬取失败')

