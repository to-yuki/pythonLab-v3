print('Hello Python',end=' ') # 最後の文字を改行からスペースへ
print('World!')

count = len('Python')
print(count) # 文字数 6

list = range(1,5,1)

count = len(list)
print(count) # 要素数 4

conv = str(123)

print('Convert String ' + conv) #文字同士の結合は可能

#print('NotConvert String ' + 123) # 文字と数値の結合は不可

i = int('123')

ans = i + 123

print(ans) # 数値同士の計算は可能

#print('123' + 123) # 文字と数値の結合は不可

f = float('123.0')
ansf = f + 123.0

print(ansf)

print('left:{:<10}'.format(ans)) # 左寄せ
print('left:{:<10}'.format(ansf)) # 左寄せ
print('center:{:^10}'.format(ans)) # 中央
print('center:{:^10}'.format(ansf)) # 中央
print('right:{:>10}'.format(ans)) # 右寄せ
print('right:{:>10}'.format(ansf)) # 右寄せ

print('{1} , {0}'.format(ansf, ans)) # 表示位置指定

exit(0) # アプリケーションの終了

