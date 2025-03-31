import math

def primeiraFuncao(x):
    return x ** 3 - 4 * x - 9
def segundaFuncao(x):
    return math.cos(math.radians(x)) - x
def terceiraFuncao(x):
    return math.log(x) + x ** 2 - 3
def quartaFuncao(x):
    return math.e ** x - 4 * x;

def primeiraFuncaoInteracao(x):
    return (4 * x + 9) ** (1/3)
def segundaFuncaoInteracao(x):
    return math.cos(math.radians(x))
def terceiraFuncaoInteracao(x):
    return math.sqrt(3-math.log(x))
def quartaFuncaoInteracao(x):
    return math.e ** x / 4