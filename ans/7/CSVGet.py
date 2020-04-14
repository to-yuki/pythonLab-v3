import codecs

# CSVファイルからデータを取得するメソッド
def get_data(file_name, encode):
    data_list = []
    with codecs.open(file_name, 'r', encode) as file:
        count = 0
        for line in file:
            if count == 0: # 1行目は日付なので、取得しない
                count += 1
            else:
                data_list.append(line.strip().split(',')) #strip()で前後の不要なエスケープ文字や空白を除去
    return data_list