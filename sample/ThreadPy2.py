import threading
from time import sleep

# threading.Thread クラスを継承
class MyThread(threading.Thread):

    # 表示メッセージ
    __msg = None
    # スリープタイム
    __sec = 1

    # スレッド化する関数
    def run(self):
        # __sec秒間隔で 'T1' を表示
        for i in range(5):
            sleep(self.__sec)
            print(self.__msg + ' '),

    # プロパティ設定関数
    def setMsgSec(self,msg,sec):
        self.__msg=msg
        self.__sec = sec

def main():
    # T1 スレッドの作成と開始
    myThread = MyThread()
    myThread.setMsgSec('T1',1)
    myThread.start()

    # T1 スレッドの作成と開始
    myThread2 = MyThread()
    myThread2.setMsgSec('T2',2)
    myThread2.start()
    
    # 各スレッドの待ち合わせ
    myThread.join()
    print('[T1 スレッド終了]')
    myThread2.join()
    print('[T2 スレッド終了]')

# メインスレッド関数を呼び出し
if __name__=='__main__':
    main()