# Non Args
def func1():
	print('	function1') #Tab Space

# 1 Args
def func2(n):
	print('	function2') #Tab Space
	print(n)

# Non Args return
def func3():
	print('	function3') #Tab Space
	n = 10
	return n

# 1 Args return
def func4(n):
	print('	function4') #Tab Space
	return n

# Call function

print('func1():')
func1()
print

print('func2(10):')
func2(10)
print

print('func3():')
i = func3()
print(i)
print

print('func4(10):')
i2 = func4(10)
print(i2)



