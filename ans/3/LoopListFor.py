import sys

# 
# 解答例は複数あります。
# 全て、リスト要素をループ処理で出力する方法です。
# 

# 解答例１ for構文１
print('for_1：')
for s in sys.argv:
    print(s)

# 解答例２ for構文2
print()
print('for_2：')
for s in sys.argv:
    for t in s:
        print(t, end = '')
    print()
