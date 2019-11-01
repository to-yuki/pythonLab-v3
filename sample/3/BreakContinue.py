print('break')
for val in [1,2,3,4,5]:
    if val == 3: 
        break # 以降の処理を中断し、反復処理を終了する
    print(val)


print('continue')
for val in [1,2,3,4,5]:
    if val == 3:
        continue #以降の処理を中断し、反復処理に戻る
    print(val)
