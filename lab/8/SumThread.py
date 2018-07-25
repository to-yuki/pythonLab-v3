import sys
from threading import Thread
from time import sleep

# 1から合計する処理を記述してください。
class SumThread(Thread):
    
    __num = 0 # 入力値
    __count = 0 # 合計値

    def __init__(self, num):
        # 属性の初期化処理を記述してください。
        pass

    def run(self):
        # 合計処理をスレッドで行うように記述してください。
        pass

def main():
        num = int(sys.argv[1])
        t = SumThread(num)
        t.start()

if __name__ == '__main__' :
    main()