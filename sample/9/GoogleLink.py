import urllib.request
from bs4 import BeautifulSoup

# 解析するWebサイトのURL
url = 'https://google.co.jp/'

# Webサイトへアクセスし、レスポンスが戻ります(<html>...</html>)
html = urllib.request.urlopen(url,cafile='cacert.pem')

# htmlドキュメントを解析
soup = BeautifulSoup(html, 'html.parser',from_encoding='UTF-8')

# タイトル Tag を取得する
title_tag = soup.title

# タイトル Tag を出力
print(title_tag)

# Taitl 要素の文字列を取得する
title = title_tag.string

# タイトルを文字列を出力
print('タイトル文字列: ' + title)
print()

# <a> を全て取得して、リンク情報を表示する
print('リンク : URL ')
list = soup.find_all('a')
for a in list:
    print(a.string,end=' ')
    print('\t: ',end=' ')
    print(a.get('href'))

# 受信データの全てを表示する
#print(soup)
