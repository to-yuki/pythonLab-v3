from Product import Product

class Appliance(Product):
    __elec_consumption = 0

    def __init__(self, code, name, price, elec_consumption):
        super().__init__(code, name, price) # スーパークラスの初期化子呼び出し
        self.__elec_consumption = elec_consumption

    def set_elec_con(self, elec_consumption):
        self.__elec_consumption = elec_consumption

    def display(self):
        super().display() # スーパークラスのメソッド呼び出し
        print('消費電力 : ', end ='')
        print(self.__elec_consumption)
