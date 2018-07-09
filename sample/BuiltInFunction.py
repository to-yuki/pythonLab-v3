# from __future__ import print_function #Python2.x

print('Hello Python',end=' ') # end='' endcode setting.
print('World!')

count = len('Python')
print(count) # count String : 6

list = range(1,5,1)

count = len(list)
print(count) # count list : 4

conv = str(123)

print('Convert String ' + conv)

#print('NotConvert String ' + 123) # Error Code

i = int('123')

ans = i + 123

print(ans)

#print('123' + 123) # Error Code

f = float('123.0')
ansf = f + 123.0

print(ansf)

print('left  : {:<10}'.format(ans)) # 左寄せ
print('left  : {:<10}'.format(ansf)) # 左寄せ
print('center: {:^10}'.format(ans)) # 中央
print('left  : {:^10}'.format(ansf)) # 中央
print('right : {:>10}'.format(ans)) # 右寄せ
print('left  : {:>10}'.format(ansf)) # 右寄せ

print('{1} , {0}'.format(ansf, ans)) # 表示位置指定

exit(0)

