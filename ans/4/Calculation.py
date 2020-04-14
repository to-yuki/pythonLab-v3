#-- Calc Function --#
def calc(val1,operator,val2):
    
    if operator == '+':
        return val1 + val2
    elif operator == '-':
        return val1 - val2
    elif operator == '*':
        return val1 * val2
    elif operator == '/':
        return val1 / val2
    else:
        raise ArithmeticError("Operator Error")