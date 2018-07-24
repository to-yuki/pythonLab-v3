class Student:
	
	__id = None # Optional Code 
	__name = None # Optional Code

	def __init__(self,id,name):
		self.__id = id
		self.__name = name
	
	def getId(self):
		return self.__id
	
	def getName(self):
		return self.__name