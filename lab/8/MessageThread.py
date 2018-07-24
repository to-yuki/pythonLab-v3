import threading, sys
from time import sleep
from threading import Thread

class MassageThread(Thread):
    __str = None
    __sec = 1
    
    def __init__(self, str):
        super().__init__() # Threadクラスの__init()__呼び出し
        self.__str = str

    def run(self):
        # pass の記述を3回ループするコードを記述してください。
        # ループ内の処理は、__sec時間停止してから__strの文字列を
        # 標準出力に表示してください。
        pass

def main():
    
    argvCount = len(sys.argv)

    for i in range(1, argvCount):
        t = MassageThread("Run! " + sys.argv[i])
        # Thread を実行するコードを記述してください。

if __name__ == "__main__" :
    main()