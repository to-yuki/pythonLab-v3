from Student import Student

# -- Main function Define--#
def main():

	st1 = Student(124,'NAO')

	id = st1.getId()
	name = st1.getName()

	print('ID : ' + str(id))
	print('NAME : ' + name)

# -- Main function Define--#
if __name__ == '__main__':
	main()
