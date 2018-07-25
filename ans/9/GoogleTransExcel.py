# -*- coding: UTF-8 -*-
import openpyxl
import requests
import re
 
# Excel ファイルをロード  
book = openpyxl.load_workbook(filename='GoogleTransExcel.xlsx',data_only=True)
# Excel シート名のリスト取得
sheetnames = book.get_sheet_names()
# 1番目のシートにアクセス
sheet = book.get_sheet_by_name(sheetnames[0])

list = []

for r in range(1,sheet.max_row+1):
    data = sheet.cell(row=r,column=1).value
    list.append(data)

# 正規表現文字列のコンパイル
pattern = re.compile(r"TRANSLATED_TEXT='(.*?)'")
# GoogleTranslateURL
url = 'https://translate.google.com/?hl=ja#en/ja/'
# 行カウンタのリセット
r = 0
# 翻訳エラー時のリトライ回数
retrycount = 3

for origin in list:
    if (origin == None or r == 0 ):
        r+=1
        continue
    # 翻訳失敗時は retrycount 回リトライする
    while(retrycount != 0):
        try:
            response = requests.get(url, params={'q': origin}) 
            # resopnse 内にある JavaScript コードから翻訳された文字列を取得
            transValue = pattern.search(response.text).group(1)
            # ExcelSheetに書き込み(list->0,excel->1)
            # 翻訳テキストの書き込み列は column で指定
            sheet.cell(row=r+1,column=2).value = transValue
            print
            print(str(r)+'行目 [translate.google.com] で翻訳') 
            print('\t英語:'),
            print(origin)
            print('\t日本語:'),
            print(transValue)
            retrycount = 3
            break
        except:
            print(str(r)+'行目翻訳リトライ。')
    else:
        print(str(r)+'行目:翻訳エラーのリトライ回数をオーバーしたので、スキップします。')
    r+=1
# ワークブックの保存
try:
    book.save('GoogleTransExcel-OK.xlsx')
except:
    print('Excelファイル保存エラーです。')