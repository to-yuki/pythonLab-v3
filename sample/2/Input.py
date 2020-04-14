from getpass import getpass # getpassモジュールのgetpass()関数の読み込み

print('Name:',end=' ')
name = input() # 標準入力から1行読み込み
print('Input Name: ',end=' ')
print(name)

password = getpass() # パスワード形式で1行読み込み
print('Input Password : ',end=' ')
print(password)
