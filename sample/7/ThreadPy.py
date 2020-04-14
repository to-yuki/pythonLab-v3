from threading import Thread
from time import sleep

# スレッド化する関数1
def thread1():
    # 1秒間隔で 'T1' を表示
    for i in range(5):
        sleep(1)
        print('T1 ',end=' ',flush=True)


# スレッド化する関数2
def thread2():
    # 2秒間隔で 'T2' を表示
    for i in range(5):
        sleep(2)
        print('T2 ',end=' ',flush=True)

# メインスレッド関数
def mainThread():
    # スレッドオブジェクトの作成
    t1 = Thread(target=thread1) # キーワード引数でスレッド化する関数を指定
    t2 = Thread(target=thread2)

    # 作成したスレッドオブジェクトの起動
    t1.start()
    t2.start()

# メインスレッド関数を呼び出し
if __name__=='__main__':
    mainThread()