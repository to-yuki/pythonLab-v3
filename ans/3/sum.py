print('整数データを入力してください　->： ', end = '')
data1 = input()

print('整数データを入力してください ->： ', end = '')
data2 = input()

data_sum = int(data1) + int(data2)

print(data1 , end=' ')
print('と',end=' ')
print(data2,end=' ')
print('の合計は ',end=' ')
print(data_sum,end=' ')
print('です。')

# format()で表示位置を指定して出力
#print('{0} と {1} の合計は {2} です。'.format(data1, data2, data_sum)) 