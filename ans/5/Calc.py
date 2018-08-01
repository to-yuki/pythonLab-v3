import sys

#-- Calc Function --#
def calc(val1,operator,val2):
    
    if operator == '+':
        return val1 + val2
    elif operator == '-':
        return val1 - val2
    elif operator == '*':
        return val1 * val2
    elif operator == '/':
        return val1 / val2
    else:
        raise ArithmeticError("Input Error")


#-- Main-Satrt --#
def main():
    try:
        val1 = int(sys.argv[1])
        operator = sys.argv[2]
        val2 = int(sys.argv[3])

        ans = calc(val1,operator,val2)

        print(str(val1) + ' ' + str(operator) + ' ' + str(val2) + ' = ' + str(ans))

    except:
        print("Input Error")

#-- Main-End --#
if __name__ == '__main__':
	main()
