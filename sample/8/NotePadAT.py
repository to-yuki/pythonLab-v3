# -*- coding: UTF-8 -*-

from datetime import datetime
from pywinauto import application
from time import sleep

#sleep time
sleepSec=1

# Win32 API(Default)
app = application.Application(backend='win32') 
app.start('notepad.exe')

# Notepad クラス (Notepad のウィンドウ) を探して日時を入力
app.Notepad.Edit.set_edit_text(datetime.now())

# メニューを選択
app.Notepad.menu_select('ファイル->名前を付けて保存')

# 「名前を付けて保存」のウィンドウを取得
nameSaveDialog = app['名前を付けて保存']

# ファイル名を設定
nameSaveDialog.Edit.set_edit_text('datetime.txt')

# 保存ボタンの取得
saveButtion = nameSaveDialog['保存(&S)']
# 保存ボタンをクリック
saveButtion.click()
# ボタンをクリック(タイミングにより反応しない場合はもう一度) 
saveButtion.click() 

# ファイルが存在すれば上書きの確認ウィンドが開く
confirmDialog = app['名前を付けて保存の確認']
# 確認Dialogウィンドが存在するかどうかの確認
if confirmDialog.exists(): 
    print('Update')
    # はいボタンの取得
    confirmButtion = confirmDialog['はい(&Y)']
    # ボタンをクリック
    confirmButtion.click()
    # ボタンをクリック(タイミングにより反応しない場合はもう一度)
    confirmButtion.click()  

# メニューの終了を選択
sleep(sleepSec) 
# Window のデータ更新が終わるのを待って終了
app.Notepad.menu_select('ファイル->メモ帳の終了')
