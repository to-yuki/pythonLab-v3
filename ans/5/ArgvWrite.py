import sys

with open(sys.argv[1], 'w') as file:
    lins = sys.argv[2:] #2番目の引数以降から切り出し
    for line in lins:
        file.write(line + '\n')
        print(line + ' を書き込みました。')

print(sys.argv[1] + ' への書き込みが完了しました。')