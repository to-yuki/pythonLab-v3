from Product import Product
from Wear import Wear
from Appliance import Appliance

def main():
    products = [Product('101', '消しゴム', 50),
                Wear('402', 'Yシャツ', 6000, 'L'),
                Appliance('901', '冷蔵庫（2ドア）', 32000, 200)]

    for product in products:
        print('----------------')
        product.display()

if __name__ == '__main__' :
    main()