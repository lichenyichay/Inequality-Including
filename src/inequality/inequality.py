from random import *
from fractions import *


def suijiine(dif:int) -> str:
    """
    Generates a random inequality expression with a given level of difficulty.
    
    Args:
        dif (int): The difficulty level of the inequality expression, which determines the number of operations.
    
    Returns:
        str: A randomly generated inequality expression.
    """
        
    opr=['+','-','*','/']
    fuhao = ['>','<','>=','<=']

    def suiji() -> str:
        op = choice(opr)
        num=randint(0,50)
        s = op + str(num)
        return s
    s = ""
    for i in range(dif):
        s = "(" + s
        if i == 0:
            s += 'x'
        s += suiji() + ")"
    s += choice(fuhao) + str(randint(0,100))
    return s
def solveine(s:str,opr:str) -> str:
    """
    Solves a given inequality expression.

    Args:
        s (str): The inequality expression to be solved.

    Returns:
        str: The solution to the inequality expression.
    """
    a = int((s.split(opr)[0]).split('+')[0][:-1])
    if "(" in s and ')' in s:
        b = int((s.split(opr)[0]).split('+')[1][1:-1])
    else:
        b = int((s.split(opr)[0]).split('+')[1])
    if a == 0:  
        # 如果a为0，则不等式变为b > 0（无解或所有实数解），或b <= 0（无解）  
        if b > 0:  
            return "所有实数"  
        else:  
            return "无解"  
    else:  
        # 计算不等式的解  
        x_value = -b / a  
        x_value = Fraction(float(x_value)).limit_denominator()
        if a > 0:  
            # 如果a为正，则解集为 x > x_value  
            return f"x > {x_value}"  
        else:  
            # 如果a为负，则解集为 x < x_value  
            return f"x < {x_value}"  
print(solveine("-9x+(-10)>0",opr='>'))