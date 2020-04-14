import sys
from time import sleep
from threading import Thread

class MessageThread(Thread):
    __str = None
    __sec = 1
    
    def __init__(self, str):
        super().__init__() # Threadクラスの__init()__呼び出し
        self.__str = str

    def run(self):
        for i in range(3):
            sleep(self.__sec)
            print(self.__str)

def main():
    
    argvCount = len(sys.argv)

    for i in range(1, argvCount):
        t = MessageThread('Run! ' + sys.argv[i])
        t.start()

if __name__ == '__main__' :
    main()