# coding: UTF-8
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
from time import sleep
import datetime
import locale
import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

locale.setlocale(locale.LC_ALL,'ja_JP')

# 日本経済新聞
url = 'https://www.nikkei.com/markets/kabu/'
try:
    # 取引時間は午前９時～11時と午後０時30分～３時
    while True:
        html = urllib.request.urlopen(url,cafile='cacert.pem')
        soup = BeautifulSoup(html, 'html.parser')
        list = soup.find_all('span')
        nikkei_heikin = None

        # 全要素の表示
        #print(soup)

        # Class='mkc-stock_prices'の検索
        for tag in list:
            try:
                classlist = tag.get('class')
                if 'mkc-stock_prices' in classlist:
                    nikkei_heikin = tag.string
                    break
            except:
                pass
        print('日経平均株価:',end=' ')
        print(datetime.datetime.today().strftime('%x %X'),end=' ')
        print('￥' + nikkei_heikin)
        sleep(60)
except KeyboardInterrupt:
    print('Ctr+C割り込みによる終了')