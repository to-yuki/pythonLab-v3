from Product import Product
import sys

def main():
	p = Product()
	p.setValue(sys.argv[1], sys.argv[2], sys.argv[3])
	code = p.getCode()
	name = p.getName()
	price = p.getPrice()
	print("商品情報は以下の通りです。")
	print("コード :" , code)
	print("名前   :" , name)
	print("価格   :" , price)

if __name__ == "__main__":
    main()