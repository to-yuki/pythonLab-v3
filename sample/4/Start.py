import Calc
#from Calc import *

def main():
	i = 10
	a = 20
	ans = Calc.add(i,a) # Calcモジュールのadd()関数呼び出し
	# ans = add(i,a) # fromを利用した関数呼び出し
	print(ans)

if __name__ == '__main__':
	main()
