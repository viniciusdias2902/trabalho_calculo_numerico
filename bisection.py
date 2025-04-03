from exibir_chutes import exibir_chutes
import functions
from gerar_csv import gerar_csv


def bissecao(f,a,b, max_iter=100):
    interacoes = []
    if (f(a) * f(b) >= 0):
        print("O produto entre f(a) e f(b) deve ser negativo \n")
        return
    c = a
    for _ in range(max_iter+1):
            if (((b-a) < 0.01)):
                 return c, interacoes
            
            c = (a+b)/2
            interacoes.append(c)
            if (f(c) == 0.0):
                break
    
            if (f(c)*f(a) < 0):
                b = c
            else:
                a = c    
    return c, interacoes

if __name__ == "__main__":
    raizPrimeiraFuncao, interacoesPrimeiraFuncao = bissecao(functions.primeiraFuncao, 2, 3)
    raizSegundaFuncao, interacoesSegundafuncao = bissecao(functions.segundaFuncao, 0, 1)
    raizTerceiraFuncao, interacoesTerceiraFuncao = bissecao(functions.terceiraFuncao, 1, 2)
    raizQuartaFuncao, interacoesQuartaFuncao = bissecao(functions.quartaFuncao, 0, 1)

    lista_interacoes = [interacoesPrimeiraFuncao, interacoesSegundafuncao, interacoesTerceiraFuncao, interacoesQuartaFuncao]

    for interacao in lista_interacoes:
        exibir_chutes(interacao, 'Método numérico: bisseção')
    gerar_csv('bisection', interacoesPrimeiraFuncao)
    gerar_csv('bisection', interacoesSegundafuncao)
    gerar_csv('bisection', interacoesTerceiraFuncao)
    gerar_csv('bisection', interacoesQuartaFuncao)
