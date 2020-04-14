import urllib.request
from bs4 import BeautifulSoup
import ssl
import locale

# CA認証局のカスタムCert設定
ctx = ssl.create_default_context(cafile='cacert.pem')
# システムロケールの指定
locale.setlocale(locale.LC_ALL,'ja_JP')

# 先頭文字列がhttpでない場合、サイトURLを付与します
def urlReplacement(str,url):
    if(str.find('//') != -1 and str.find('http') == -1):
        return 'https:'+str # URLの先頭が//で始まっている場合プロトコルの追加
    elif(str.find('http') == -1):
        return url+str # URLがhttpで始まっていな場合サイトアドレスの追加
    else:
        return str

try:
# 解析するWebサイトのURL(最後の/は入力しない)
    url = 'https://www.disney.co.jp'
    # url = 'http://yahoo.co.jp'
    # Webサイトへアクセスし、レスポンスが戻ります(<html>...</html>)
    html = urllib.request.urlopen(url,context=ctx)
    # htmlドキュメントを解析
    soup = BeautifulSoup(html, 'html.parser')
    # タイトル Tag を取得する
    title_tag = soup.title
    # Taitl 要素の文字列を取得する
    title = title_tag.string
    # タイトルを文字列を出力
    print(title+' サイトの画像リンクを回収します。')
    # <a> を全て取得して、リンク情報を表示する
    list = soup.find_all('img')
    
    # 保存ファイル名
    filename='imageLinks.csv'

    with open(filename,'w') as f:
        for img in list:
            str =  img.get('src')+'\n'
            str =  urlReplacement(str,url)    
            f.write(str)
    print(filename + ' ファイルにサイトの画像リンクを回収完了。')
    # 受信データの全てを表示する
    # print soup.encode('cp932')
except Exception as e:
    print('IOError: ReTry please!' + str(e))