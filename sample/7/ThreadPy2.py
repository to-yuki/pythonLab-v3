from threading import Thread
from time import sleep

# threading.Thread クラスを継承
class MyThread(Thread):

    # 表示メッセージ
    __msg = None
    # スリープ時間
    __sec = 1

    # スレッド化する関数
    def run(self):
        # __sec秒間隔で__msgを表示
        for i in range(5):
            sleep(self.__sec)
            print(self.__msg + ' '),

    # プロパティ設定関数
    def setMsgSec(self,msg,sec):
        self.__msg = msg
        self.__sec = sec

def main():
    myThread = MyThread() # スレッドのインスタンス化
    myThread.setMsgSec('T1',1)
    myThread.start() # スレッドの起動

    myThread2 = MyThread() # スレッドのインスタンス化
    myThread2.setMsgSec('T2',2)
    myThread2.start() # スレッドの起動
    
    myThread.join() # myThreadスレッドの終了待ち合わせ
    print('[T1 スレッド終了]')
    myThread2.join() # myThread2スレッドの終了待ち合わせ
    print('[T2 スレッド終了]')

# メインスレッド関数を呼び出し
if __name__=='__main__':
    main()