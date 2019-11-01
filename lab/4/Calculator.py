import sys
from Calculation import calc

#-- Main-Satrt --#
def main():
    try:
        val1 = int(sys.argv[1])
        operator = sys.argv[2]
        val2 = int(sys.argv[3])

        #Calculation.pyのcalculation()関数を完成させてください。
        ans = calc(val1,operator,val2)

        print(str(val1) + ' ' + str(operator) + ' ' + str(val2) + ' = ' + str(ans))

    except:
        print("Input Error")

#-- Main-End --#
if __name__ == '__main__':
	main()
