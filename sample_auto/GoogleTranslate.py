# -*- coding: UTF-8 -*-
import requests
import re
 
origin = u'Automate your work with Python.'
url = u'https://translate.google.com/?hl=ja#en/ja/'
response = requests.get(url, params={'q': origin})

# 受信データを全て表示する
#print(response.text)

# resopnse 内にある JavaScript コードから翻訳された
# 文字列を取得 TRANSLATED_TEXT='(翻訳されて文字列)'
pattern = r"TRANSLATED_TEXT='(.*?)'"
transValue = re.search(pattern,response.text).group(1)

print('[translate.google.com] で翻訳') 
print('英語:',end=' ') 
print(origin)
print('日本語:',end=' ') 
print(transValue)
