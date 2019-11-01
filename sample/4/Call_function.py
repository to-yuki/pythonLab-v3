# 引数無し、戻り値無し
def greeting():
	print('Hello')

# 引数1つ、戻り値無し
def sayHello(name):
	print('Hello ',end='')
	print(name)

# 引数なし、戻り値1つ
def createNumber():
	return 100

# 引数1つ、戻り値1つ
def doubleNumber(number):
	return number*2

# ここから関数の呼び出し

print('greeting():')
greeting()
print()

print('sayHello("Python"):')
sayHello('Python')
print()

print('createNumber():')
i = createNumber()
print(i)
print()

print('doubleNumber(10):')
i2 = doubleNumber(10)
print(i2)



