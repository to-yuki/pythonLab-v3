from datetime import datetime
from pywinauto import application
from time import sleep

# Win32 API(Default 32bit App)
app = application.Application(backend='win32') 

app.start('notepad.exe')
# アプリケーションのプロセスID
print(app.process)

# 起動したアプリの Top Window の取得
#mainDialog = app.top_window_() # TopWindow のダイアログ取得
#mainDialog = app.Notepad # コンポーネント指定のダイアログ取得
mainDialog = app['無題 - メモ帳'] # 指定 taitle のダイアログ取得
mainDialog.print_control_identifiers()

print('=========================================')

# Main Window のメニュー操作(フォントダイアログを開く)
mainDialog.menu_select('書式->フォント')

# フォントダイアログの取得と制御要素の表示
fontDialog = app['フォント']
fontDialog.print_control_identifiers()

# アプリケーションのプロセスの kill
app.kill()
