class Employee: # Employeeクラスの定義（スーパークラス）
	
	__salary=0 # 給料

	def setSalary(self,amount): # 給料設定用メソッド
		self.__salary=amount
 
	def dispSalary(self):
		print('Total Salary  --> ' + str(int(self.__salary)))

class Manager(Employee): # Managerクラスの定義（サブクラス）
	def setSalary(self,amount): # 給料設定用メソッドのオーバーライド
		super().setSalary(amount*1.5) # Managerの場合には給料を1.5倍にする

objs = [Employee(),Manager()] # EmployeeとManagerが混在するリスト

for o in objs:
	print('----' + str(o)) # 対象のオブジェクトを文字列化
	print('setSalary(300000.0):'),
	o.setSalary(300000.0)  # ポリモフィズムを使用した同名のメソッド呼び出し
	print('dispSalary():')
	o.dispSalary()
