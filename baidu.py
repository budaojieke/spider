# -*- coding:utf-8 -*-
import re
import requests
import uuid

global num
def dowmloadPic(html, keyword):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i=0
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    for each in pic_url:
        print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
        try:
            pic = requests.get(each, timeout=2)
        except :
            print('【错误】当前图片无法下载')
            continue

        dir = 'images/' + keyword + '_' + str(uuid.uuid1()) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1


if __name__ == '__main__':
    word = input("Input key word: ")
    pages = input("input pages :")

    for page in range(1, int(pages)):
        url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip' + '&pn=' + str(page*30)
        result = requests.get(url)
        dowmloadPic(result.text, word)