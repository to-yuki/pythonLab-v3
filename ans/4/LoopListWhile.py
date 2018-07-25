import sys

# 
# 解答例は複数あります。
# 全て、リスト要素をループ処理で出力する方法です。
# 

# 解答例1 while構文1
print('')
print('while_1：')
i = 0
while i < len(sys.argv):
    print(sys.argv[i])
    i += 1

# 解答例2 while構文2
print('')
print('while_2：')
i = 0
r = 0
while i < len(sys.argv):
    while r < len(sys.argv[i]):
        print(sys.argv[i][r], end = '')
        r += 1
    i += 1
    r = 0
    print('')