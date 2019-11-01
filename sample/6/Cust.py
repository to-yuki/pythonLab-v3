class Customer: # クラス定義
	__name = None # 省略可能
	__no = None # 省略可能

	def __init__(self,name,no): #初期化子の定義
		self.__name = name
		self.__no = no
	
	def getName(self):
		return self.__name
	
	def getNo(self):
		return self.__no

