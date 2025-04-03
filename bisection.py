from exibir_chutes import exibir_chutes
import functions
from gerar_csv import gerar_csv


def bissecao(f,a,b, max_iter=100, tol=1e-6):
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
            if (abs(f(c)) < tol):
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

    for index, interacao in enumerate(lista_interacoes):
        gerar_csv(f'bisection_{index+1}', interacao)        
        exibir_chutes(interacao, 'Método numérico: bisseção')
