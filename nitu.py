# http://www.nipic.com/
import os
import urllib
import urllib.request
from bs4 import BeautifulSoup
import time
import socket
from urllib.parse import quote
import string

socket.setdefaulttimeout(2)
path = 'E:/source/sky/'
if not os.path.exists(path):
    os.makedirs(path)

keyword = input('输入关键字：')
SEARCH_URL = 'http://soso.nipic.com/?q={}&g=0&or=0&y=48'.format(keyword)
SEARCH_URL = quote(SEARCH_URL, safe = string.printable)
pages = int(input('输入搜索页数：'))
for page in range(1, pages + 1):
    seach_url = SEARCH_URL + '&page={}'.format(page)
    try:
        req = urllib.request.Request(seach_url)
        webpage = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        print("open", seach_url, "fail")
        continue
    # else:
    #     print("open", seach_url, "success")
    html = webpage.read()
    soup = BeautifulSoup(html, features="html.parser")
    for k in soup.find_all('a', class_='search-works-name'):
        # print(k['href'])
        try:
            req1 = urllib.request.Request(k['href'])
            webpage1 = urllib.request.urlopen(req1)
        except:
            print("open", k['href'], "fail")
            continue
        # else:
        #     print("open", k['href'], "success")
        try:
            html1 = webpage1.read()
            soup1 = BeautifulSoup(html1, features="html.parser")
        except:
            pass
        for j in soup1.find_all('img', class_='works-img'):
            img_name  = j['src'].split('/')[-1]
            try:
                urllib.request.urlretrieve(j['src'], path + img_name)
                print('page:', page , j['src'], '--->', img_name)
            except:
                print('fail download')

        time.sleep(0.2)



