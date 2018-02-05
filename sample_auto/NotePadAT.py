# -*- coding: UTF-8 -*-

from datetime import datetime
from pywinauto import application
from time import sleep

#sleep time
sleepSec=1

# Win32 API(Default)
app = application.Application(backend="win32") 
app.start("notepad.exe")

# Notepad クラス (Notepad のウィンドウ) を探して日時を入力
app.Notepad.Edit.SetText(unicode(datetime.now()))

# メニューを選択
app.Notepad.MenuSelect(u"ファイル->名前を付けて保存")

# 「名前を付けて保存」のウィンドウを取得
nameSaveDialog = app[u"名前を付けて保存"]

# ファイル名を設定
nameSaveDialog.Edit.SetText(u"datetime.txt")

# 保存ボタンの取得
saveButtion = nameSaveDialog[u'保存(&S)']
# 保存ボタンをクリック
saveButtion.Click()
# ボタンをクリック(タイミングにより反応しない場合はもう一度) 
saveButtion.Click() 

# ファイルが存在すれば上書きの確認ウィンドが開く
confirmDialog = app[u"名前を付けて保存の確認"]
# 確認Dialogウィンドが存在するかどうかの確認
if confirmDialog.Exists(): 
    print 'Update'
    # はいボタンの取得
    confirmButtion = confirmDialog[u'はい(&Y)']
    # ボタンをクリック
    confirmButtion.Click()
    # ボタンをクリック(タイミングにより反応しない場合はもう一度)
    # confirmButtion.Click()  

# メニューの終了を選択
sleep(sleepSec) 
# Window のデータ更新が終わるのを待って終了
app.Notepad.MenuSelect(u"ファイル->メモ帳の終了")