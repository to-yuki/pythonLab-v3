# -*- coding: UTF-8 -*-
import urllib2
from bs4 import BeautifulSoup

# 解析するWebサイトのURL
url = "http://google.co.jp/"

# Webサイトへアクセスし、レスポンスが戻ります(<html>...</html>)
html = urllib2.urlopen(url)

# htmlドキュメントを解析
soup = BeautifulSoup(html, "html.parser")

# タイトル Tag を取得する
title_tag = soup.title

# タイトル Tag を出力
print title_tag

# Taitl 要素の文字列を取得する
title = title_tag.string

# タイトルを文字列を出力
print("title: " + title)

# <a> を全て取得して、リンク情報を表示する
list = soup.find_all("a")
for a in list:
    try:
        print(a.string.encode('cp932')),
    except:
        print('???'), # Tagの要素文字列なし
    print("\t: "),
    print(a.get("href").encode('cp932'))

# 受信データの全てを表示する
# print soup.encode('cp932')
