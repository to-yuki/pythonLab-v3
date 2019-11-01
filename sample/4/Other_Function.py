# デフォルト引数
def funcDefArg(x=0,y=0):
	print(x)
	print(y)

funcDefArg()

# 任意引数
def funcMultiArg(*n):
	print(n)
	print(n[2])

funcMultiArg(10,20,30,40)

def funcKeyArg(id='null',name='null'):
	print(id)
	print(name)
# キーワード引数を使用した呼び出し
funcKeyArg(name='Yamada',id='001')

# ラムダ式
f = lambda x: x + 1
ans = f(5)
print(ans)
