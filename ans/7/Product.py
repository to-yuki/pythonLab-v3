class Product:
    __code = None
    __name = None
    __price = 0

    def __init__(self, code=None, name=None, price=None):
        self.__code = code
        self.__name = name
        self.__price = price

    def display(self):
        print("商品情報は以下の通りです。")
        print("コード : ", end ="")
        print(self.__code)
        print("名前   : ", end ="")
        print(self.__name)
        print("価格   : ", end ="")
        print(self.__price)
    
    def setValue(self, code, name, price):
        self.__code = code
        self.__name = name
        self.__price = price

    def getCode(self):
        return self.__code
    
    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
        