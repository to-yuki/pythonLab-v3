import threading, sys, random
from CSVGet import get_data
from time import sleep
import pprint

class CityThread(threading.Thread):
    __data_list = []
    __nissho_sum = 0
    
    def __init__(self, data_list):
        super().__init__() # Threadクラスの__init__()呼び出し
        self.__data_list = data_list
        self.name = data_list[0] # スレッドに名前を付けられるので都市名にする。付けた名前はgetName()で取得できる

    def run(self):
        for data in self.__data_list:
            try:
                self.__nissho_sum += float(data)
            except:
                pass
        # ゆっくり動作を確認した場合はコメントを外してください。
        # sleep(random.randint(1, 3)) # 数秒間スレッドを休止する（ランダム）
        print('{0:<4}の計算が完了しました。: 総日照時間 {1}'.format(self.getName(),self.__nissho_sum))
    
    def join(self):
        super().join()
        return self.getName(), self.__nissho_sum # 待合せ後、計算結果を戻り値で取得

def main():
    try:
        sum_map = {}
        thread_list = []

        # CSVデータの取得
        source_data = get_data(sys.argv[1], sys.argv[2])
        # 各都市毎にスレッドを生成して起動し、計算させる
        for l in source_data:
            t = CityThread(l)
            thread_list.append(t)
            t.start()
    
        # スレッドでの計算結果取得
        for i in range(len(thread_list)):
            data = thread_list[i].join() # タプル型で結果取得
            sum_map[data[0]] = data[1] # 辞書型データでsum_mapへ格納
        
        #print('')
        #pprint.pprint(sum_map) # pprint()で辞書型データを整形して出力
        print()
        maxValue = max(sum_map.values()) # Valueのなかで一番大きい数値を取得
        print('{0:<23}{1} 時間'.format('総日照時間が多い都市の値は:', maxValue))
        minValue = min(sum_map.values()) # Valueのなかで一番小さい数値を取得
        print('{0:<22}{1} 時間'.format('総日照時間が少ない都市の値は:', minValue))
    
    except:
        print('Error: Please input a File name and Encode.')

if __name__ == '__main__':
    main()