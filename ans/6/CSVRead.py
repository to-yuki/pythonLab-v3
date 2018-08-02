import codecs, sys

# エンコードを指定して、ファイルを開く
with codecs.open(sys.argv[1], 'r', sys.argv[2]) as file:
    list = []
    age_sum = 0
    row_count = 0

#一行ずつ取り出し、リスト型に格納する
    for line in file:
        list = line.strip().split(',') # 行末の不要な文字列（\r\n）はsplit()で除去できる
        try:
            age_sum += int(list[3]) # 年齢だけ数値型に変換して、加算
            row_count += 1 # 数値変換できた回数を数える（= メンバー数）
        except:
            continue

age_mean = age_sum / row_count
print('年齢（平均）: {0}'.format(age_mean))