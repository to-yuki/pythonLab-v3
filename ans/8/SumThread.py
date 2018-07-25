import sys
from threading import Thread
from time import sleep

class SumThread(Thread):
    
    __num = 0 # 入力値
    __count = 0 # 合計値

    def __init__(self, num):
        super().__init__()
        self.__num = num

    def run(self):
        for i in range(1, self.__num + 1):
            print(i, end = '')
            print(' を加算します。')
            sleep(1)
            self.__count += i
        print('')
        print('計算結果は ', end = '')
        print(self.__count)

def main():
        num = int(sys.argv[1])
        t = SumThread(num)
        t.start()

if __name__ == '__main__' :
    main()