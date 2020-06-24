import os
import urllib
import urllib.request
from bs4 import BeautifulSoup
import time
from urllib.parse import quote
import string
import socket

socket.setdefaulttimeout(2)

path = 'E:/source/624/'
if not os.path.exists(path):
    os.makedirs(path)

keyword = input('输入关键字：')
SEARCH_URL = r"https://www.vcg.com/creative/search?phrase={}".format(keyword)
SEARCH_URL = quote(SEARCH_URL, safe = string.printable)

pages = int(input('输入搜索页数：'))
for page in range(7, pages + 1):
    index = 1
    # seach_url = SEARCH_URL + '&page={}'.format(page)
    seach_url = 'https://www.vcg.com/creative/search?phrase=%E8%93%9D%E5%A4%A9&page=8'
    try:
        req = urllib.request.Request(seach_url)
        webpage = urllib.request.urlopen(req)
    except:
        print("open", seach_url, "fail")
        continue
    print("open", seach_url, "success")
    try:
        html = webpage.read()
        soup = BeautifulSoup(html, features="html.parser")
    except:
        continue

    for k in soup.find_all('img', class_='lazyload_hk'):
        # print(k['data-src'])
        img_name = k['data-src'].split('/')[-1]
        try:
            urllib.request.urlretrieve('https:' + k['data-src'], path + img_name)
            print('page:', page, 'index :', index, k['data-src'], '--->', img_name)
            index += 1
        except:
            print('fail download')
        time.sleep(0.1)
