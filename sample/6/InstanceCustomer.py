from Cust import Customer # CustモジュールのCustomerクラスをインポート

def main():

	cust1 = Customer('A','001') # Aさんのインスタンス化

	name = cust1.getName() # Aさんのメソッド呼び出し
	no = cust1.getNo() # Aさんのメソッド呼び出し

	print('Name : ' + name)
	print('No : ' + no)

	print('------------------')

	cust2 = Customer('B','002') # Bさんのインスタンス化

	name = cust2.getName() # Bさんのメソッド呼び出し
	no = cust2.getNo() # Bさんのメソッド呼び出し

	print('Name : ' + name)
	print('No : ' + no)

	print('------------------')

	cust1.newVal = 100 # Aさんのインスタンスに新しい変数を追加

	print(cust1.newVal) # 追加した変数へのアクセス
	#print(cust2.newVal)  # Bさんのインスタンスには存在しないためエラー
	#print(cust1.__name)    # private変数のためエラー
	print(cust1._Customer__name) # _クラス名__変数名でアクセス可能

# -- Main function Define--#
if __name__ == '__main__':
	main()
