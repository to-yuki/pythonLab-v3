def deco_num(func):
    def wrapper(*args):
        print('ans =',end=' ')
        result = func(*args)
        return result
    return wrapper

@deco_num
def add_num(a,b):
    return a + b

@deco_num
def sub_num(a,b):
    return a - b

r = add_num(10,20)
print(r)

r = sub_num(10,20)
print(r)
