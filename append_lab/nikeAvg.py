# coding: UTF-8
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
from time import sleep
import datetime
import locale

locale.setlocale(locale.LC_ALL,"Japanese")

# 日本経済新聞
url = "http://www.nikkei.com/markets/kabu/"
try:
    while True:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        list = soup.find_all("span")
        nikkei_heikin = None

        # 全要素の表示
        #print(soup)

        # Class="mkc-stock_prices"の検索
        for tag in list:
            try:
                classlist = tag.get("class")
                if "mkc-stock_prices" in classlist:
                    nikkei_heikin = tag.string
                    break
            except:
                pass
        print("日経平均株価:",end=' ')
        print(datetime.datetime.today().strftime("%x %X"),end=' ')
        print("￥" + nikkei_heikin)
        sleep(60)
except KeyboardInterrupt:
    print(u"Ctr+C割り込みによる終了")