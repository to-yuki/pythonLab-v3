from Product import Product

class Wear(Product):
    __size = None

    def __init__(self, code, name, price, size):
        super().__init__(code, name, price) # スーパークラスの初期化子呼び出し
        self.__size = size

    def set_size(self, size):
        self.__size = size

    def display(self):
        super().display() # スーパークラスのメソッド呼び出し
        print('サイズ   : ', end ='')
        print(self.__size)

