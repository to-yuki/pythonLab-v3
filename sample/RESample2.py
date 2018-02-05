# -*- coding: UTF-8 -*-
import re

requestString = u"https://www.google.co.jp/search?hl=ja&source=hp&biw=&bih=&q=Python&btnG=Google+%E6%A4%9C%E7%B4%A2&gbv=1"

# 先頭から http://(何でもよい文字列) にマッチするものを取得
match = re.match(r"https://(.*)\?(.*)",requestString)
# マッチグループの1つ目
print(u"マッチ文字列 : " + match.group())
print(u"マッチ文字列 グループ1 : " + match.group(1))

# split("&") を使用して、key=value のリストに分解
matchGroup2 = match.group(2)
print(u"マッチ文字列 グループ2 : " + matchGroup2)

print(u"マッチ文字列 グループ2 を split(\"&\") で分解")
list = matchGroup2.split("&")
for s in list:
    print("\t" + s)

# 文字列全体から q=(何でもよい)& にマッチするものを取得
print(u"全体から q= の値を取得")
result = re.search(r"q=(.*?)&",requestString).group(1)
print(result)


