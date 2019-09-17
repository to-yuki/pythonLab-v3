from Product import Product
import sys

def main():
    
    try:
        productlist = [
            Product('001', 'ペン', 100),   
            Product('002', '消しゴム', 150),
            Product('003', 'ファイルボックス', 500)
            ]

        for p in productlist:
            if sys.argv[1] == p.getCode():
                p.display()
                break
        else:
            print('Unexpected number was inputted.')
    except:
        print('Unexpected arguments were inputted.')

if __name__ == '__main__' :
    main()
