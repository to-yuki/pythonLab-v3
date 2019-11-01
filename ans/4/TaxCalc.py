import sys

# 税計算関数
def taxCalc(price,tax=0.0):
    return price * (1+tax)

# main関数
def main():
    try:
        price = int(sys.argv[1])
        tax = float(sys.argv[2])

        totalFee = taxCalc(price,tax)
        print('Price :',price)
        print('Tax :',tax)
        print('Total Fee :',totalFee)
    except:
        print("Input Error")

if __name__ == '__main__':
	main()
