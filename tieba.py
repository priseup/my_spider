# -*- coding: utf-8 -*-
# feimengjuan
import re
import os
import requests
from bs4 import BeautifulSoup

def getHtml(url):
    r = requests.get(url)
    return r

# 输入文件名，保存多张图片
def saveImages(imglist, prex, suffix):
    number = 1

    # print(imglist)
    for src in imglist:
        fileName = prex + '_' + str(number) + suffix

        image = requests.get(src)
        with open(fileName, 'wb') as f:
            f.write(image.content)

        number += 1

def getAllImg(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    all = soup.find_all('img', class_='BDE_Image')  # returns a list
    images = []
    for a in all:
        imagesrc = a['src']
        if imagesrc not in images:
            images.append(imagesrc)

    return images


if __name__ == '__main__':
    html = getHtml("http://tieba.baidu.com/p/2460150866")
    imglist = getAllImg(html)
    saveImages(imglist, 'tieba', '.jpg')
