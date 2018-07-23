# default Arg
def funcDefArg(x=0,y=0):
	print(x),
	print(y)

funcDefArg()

# MultiArgs
def funcMultiArg(*n):
	print(n),
	print(n[2])

funcMultiArg(10,20,30,40)

# KeyArg
def funcKeyArg(id='null',name='null'):
	print(id),
	print(name)

fu ncKeyArg(name='Yamada',id='001')

# lambda 
f = lambda x: x + 1
ans = f(5)
print(ans)
