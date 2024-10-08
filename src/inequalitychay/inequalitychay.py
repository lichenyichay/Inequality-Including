from random import *
from fractions import *


def suijiine(dif:int,maxnum:int,minnum:int,maxn:int,minn:int,te:list) -> str:
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
        if te != []:
            if op in te:
                num = randint(minn,maxn)
            else:
                num = randint(minnum,maxnum)
        else:
            num = randint(minnum,maxnum)
        s = op + str(num)
        return s
    s = ""
    for i in range(dif):
        s = "(" + s
        if i == 0:
            s += 'x'
        s += suiji() + ")"
    s += choice(fuhao) + str(randint(0,50))
    return s
def solveine(s:str) -> str:
    """
    Solves a linear inequality expression and returns the solution set.
    
    Args:
        s (str): The inequality expression as a string.
    
    Returns:
        str: The solution set of the inequality expression.
    """
    op=['>','<',">=",'<=']
    for i in op:
        if i in s:
            opr = i
            break
    else:
        raise ValueError("It is not a linear inequality.")
    a = int((s.split(opr)[0]).split('+')[0][:-1])
    if "(" in s and ')' in s:
        b = int((s.split(opr)[0]).split('+')[1][1:-1])
    else:
        b = int((s.split(opr)[0]).split('+')[1])
    if a == 0:  
        # 如果a为0，则不等式变为b > 0（无解或所有实数解），或b <= 0（无解）  
        if opr == '>':
            if b > 0:  
                return "所有实数"  
            else:  
                return "无解"  
        elif opr == '<':
            if b < 0:
                return "所有实数"
            else:
                return "无解"
        elif opr == '>=':
            if b >= 0:
                return "所有实数"
            else:
                return "无解"
        elif opr == '<=':
            if b <= 0:
                return "所有实数"
            else:
                return "无解"
    else:  
        # 计算不等式的解  
        x_value = -b / a  
        x_value = Fraction(float(x_value)).limit_denominator()
        if a > 0: 
            return f"x {opr} {x_value}"  
        else:  
            if opr == '>' or opr == '>=':
                return f"x {op[op.index(opr)+1]} {x_value}"
            else:
                return f"x {op[op.index(opr)-1]} {x_value}"