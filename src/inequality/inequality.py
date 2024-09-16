from random import *

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
