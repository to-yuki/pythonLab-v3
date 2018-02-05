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

# Non Args
def func1():
    print(' function1')

# 1 Args
def func2(n):
    print(' function2'),
    print(n)

# Non Args return
def func3():
    print(' function3')
    n = 10
    return n

# 1 Args return
def func4(n):
    print(' function4')
    return n

