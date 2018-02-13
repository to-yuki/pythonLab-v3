import pyautogui as gui
from pywinauto import application
from time import sleep

# Windowsサイズの取得
w,h = gui.size()
print('Windows Size : ' + str(w) + ' x ' + str(h))

 # 現在のマウスポジションの取得
x,y = gui.position()
print('Current x,y : ' + str(x) + ',' + str(y))

# Paintアプリケーションに描画する
mspaint = application.Application()
mspaint.start('mspaint.exe')
sleep(3)
select = gui.confirm(text='ペイントアプリを画面中央表示して、\n直線を選択してください。', title='確認！',buttons=['OK', 'Cancel'])
if select in 'OK':
    # マウスカーソルの中央への移動
    gui.moveTo(x=(w/2),y=(h/2))
    x,y = gui.position()
    print('Point after moving x,y : ' + str(x) + ',' + str(y))
    gui.dragTo(x=(x/2)+100,y=(y/2)+100,button='left')
    # gui.mouseDown(button='left')
    # gui.mouseUp(button='left',x=(x/2)+100,y=(y/2)+100)

# スクリーン範囲の確認
check = gui.onScreen(100,100)
if check:
    print('x=100,y=100 ' + 'onScreen')
else:
    print('x=2000,y=3000 ' + 'off onScreen')

gui.alert(text='処理終了',title='確認！',button='OK')

# アプリケーションのプロセスの kill
mspaint.kill()
