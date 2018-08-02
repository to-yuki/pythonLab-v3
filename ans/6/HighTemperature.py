import codecs, sys

# 2つの値を比較する関数。戻り値は二つの値を受け取る
def compair(val1, val2):
    if val1 > val2:
        return val1
    else:
        return val2

date = [] # 日付を格納するリスト
data_list = [] # 各都市ごとの日付データを格納するリスト
with codecs.open(sys.argv[1], 'r', sys.argv[2]) as file:
    count = 0
    for line in file:
        if count == 0: # 1行目の日付データのみ、別に格納する
            date = line.strip().split(',')
            count += 1
        else:
            data_list.append(line.strip().split(',')) #strip()で行末の不要の文字列を除去

for city_data in data_list:
    # リスト型データの先頭の要素は都市名
    print(city_data[0], end = ' : ')
    # 順番に気温データを取得し、小数データに変換。二つの数値を比較し、大きいデータをhighに格納していく
    high = float(city_data[1])
    highIndex = 1
    for i in range(2, len(city_data)):
        # 引数に比較したい二つの気温の値を渡す
        high = compair(high, float(city_data[i]))
        # 高い気温の要素番号を記録しておく
        if high == float(city_data[i]):
            highIndex = i
    # 要素番号を利用して、日付も取得する
    print('{0} ℃ ({1})'.format(high, date[highIndex]))
