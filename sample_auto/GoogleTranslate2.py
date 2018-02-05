# -*- coding: UTF-8 -*-
import urllib2
from urllib import urlencode
from bs4 import BeautifulSoup

res = urllib2.urlopen('https://translate.google.com/?hl=ja#en/ja/q=aa')
print res.read()



# 解析するWebサイトのURL
#url = u'https://translate.google.com/?hl=ja#en/ja/'
#origin = u'Automate your work with Python.'
#url = url + origin

#print(url)

#html = urllib2.urlopen(url)

# htmlドキュメントを解析
#soup = BeautifulSoup(html, "html.parser")

#print(soup)
