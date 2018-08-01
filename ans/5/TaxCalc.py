import sys

#-- taxCalc Function --#
def taxCalc(price,tax=0):
    return price * (1+tax)

#-- Main-Satrt --#
def main():
    try:
        price = int(sys.argv[1])
        tax = int(sys.argv[2])

        taxCalc(price,tax)
    except:
        print("Input Error")

#-- Main-End --#
if __name__ == '__main__':
	main()
