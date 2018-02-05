class Customer:
	
	__name = None # Optional Code 
	__no = None # Optional Code

	def __init__(self,name,no):
		self.__name = name
		self.__no = no
	
	def getName(self):
		return self.__name
	
	def getNo(self):
		return self.__no

