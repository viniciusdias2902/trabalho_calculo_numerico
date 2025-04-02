import math

def primeiraFuncao(x):
    return x ** 3 - 4 * x - 9
def segundaFuncao(x):
    return (math.cos(x)) - x;
def terceiraFuncao(x):
    return math.log(x) + x ** 2 - 3
def quartaFuncao(x):
    return math.e ** x - 4 * x;

def primeiraFuncaoInteracao(x):
    return (4 * x + 9) ** (1/3)
def segundaFuncaoInteracao(x):
    return math.cos(x)
def terceiraFuncaoInteracao(x):
    return math.sqrt(3-math.log(x))
def quartaFuncaoInteracao(x):
    return math.e ** x / 4

def derivadaPrimeiraFuncao(x):
    return 3 * (x ** 2) - 4
def derivadaSegundaFuncao(x):
    return -math.sin(x) - 1
def derivadaTerceiraFuncao(x):
    return 2 * x + 1/x
def derivadaQuartaFuncao(x):
    return math.e ** x - 4