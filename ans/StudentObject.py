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

# -- Main function Define--#
def main():

	st1 = Student(124,'NAO')

	id = st1.getId()
	name = st1.getName()

	print('ID : ' + str(id))
	print('NAME : ' + name)

# -- Main function Define--#
if __name__ == "__main__":
	main()
