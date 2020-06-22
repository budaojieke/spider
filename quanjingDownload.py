# -*- coding:utf-8 -*-
import os
import time
import requests
import urllib
import uuid
from pyquery import PyQuery
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/83.0.4103.106 Safari/537.36",
    "Referer": "https://www.quanjing.com/search.aspx?q=%E6%A2%A8%20%E8%A5%BF%E6%B4%8B%E6%A2%A8"
}


def href_url_download():
    # 1.填写要爬取关键词的list.txt
    keyword_list = open("list.txt", 'r', encoding='utf-8')
    lines = keyword_list.readlines()
    keyword_list.close()
    for keyword in lines:
        keyword = keyword.strip()
        print(keyword)
        # 2.修改爬取的页数(1,101),默认爬取100页
        for pages in range(1, 2000):
            page = str(pages)
            # json结构分析：F12->Network->XHR->Headers->Request URL ！
            # json结构分析：F12->Network->XHR->Headers->Request Headers -> Referer(添加到请求头) ！
            # url = "https://www.quanjing.com/Handler/SearchUrl.ashx?t=9056&callback=searchresult" \
            #       "&q=%E8%8B%B9%E6%9E%9C&stype=1&pagesize=100&pagenum=2&imageType=2&imageColor=&brand=&imageSType=" \
            #       "&fr=1&sortFlag=1&imageUType=&btype=&authid=&_=1568188675552 "
            url = "https://www.quanjing.com/Handler/SearchUrl.ashx?t=9056&callback=searchresult&q=" + keyword + \
                  "&stype=1&pagesize=100&pagenum=" + page + "&imageType=2&imageColor=&brand=&imageSType=&fr=1&" \
                                                            "sortFlag=1&imageUType=&btype=&authid=&_=1568188675552"
            # print(url)
            try:
                txt = requests.get(url, headers=headers).text  # 获取URL及headers
                # print(txt[13:-1]) # 切块！
                json_txt = json.loads(txt[13:-1])
                # print(json_txt)
                product_list = json_txt.get("imglist")
                # print(product_list)
                for product in product_list:
                    image_url = product.get("imgurl")
                    print(image_url)
                    image_download(keyword, image_url)  # 下载"图片"
            except requests.exceptions.ConnectionError as e:
                print("requests.exceptions.ConnectionError")


def image_download(keyword, image_url):
    # 3.图片存储路径
    folder_path = "./image/" + keyword + "/"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        # print(folder_path)
    image = keyword + "_" + str(uuid.uuid1()) + ".jpg"  # 图片命名
    print(image)
    # urllib.request.urlretrieve(href3, folder_path + "/" + image)
    try:
        content = requests.get(image_url, headers=headers)
        with open(folder_path + image, "wb") as f:
            f.write(content.content)
    except urllib.error.HTTPError:
        print("Internal Server Error")
    except requests.exceptions.ConnectionError as e:
        print("requests.exceptions.ConnectionError")


if __name__ == '__main__':
    href_url_download()
