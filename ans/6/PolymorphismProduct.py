from Wear import Wear
from Appliance import Appliance

def main():
    
    product = Wear('400', 'Tシャツ（婦人）', 3900, 'S')
    product.display()

    product = Appliance('900', 'テレビ（32インチ）', 49800, 120)
    product.display()

if __name__ == '__main__' :
    main()