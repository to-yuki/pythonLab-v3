from Customer import Customer

def main():

	cust1 = Customer('A','001')

	name = cust1.getName()
	no = cust1.getNo()

	print('Name : ' + name)
	print('No : ' + str(no))

	print('------------------')

	cust2 = Customer('B','002')

	name = cust2.getName()
	no = cust2.getNo()

	print('Name : ' + name)
	print('No : ' + str(no))

	print('------------------')

	cust1.newVal = 100

	print(cust1.newVal)
	#print(cust2.newVal)  # Error Code

	#print(cust1.__name)    # __ Private Access

# -- Main function Define--#
if __name__ == '__main__':
	main()

