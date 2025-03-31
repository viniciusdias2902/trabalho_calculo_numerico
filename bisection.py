import functions
import gerar_csv


def bissecao(f,a,b, max_iter=25):
    interacoes = []
    if (f(a) * f(b) >= 0):
        print("O produto entre f(a) e f(b) deve ser negativo \n")
        return
    c = a
    for _ in range(max_iter):
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

raizPrimeiraFuncao, interacoesPrimeiraFuncao = bissecao(functions.primeiraFuncao, 2, 3)
print(raizPrimeiraFuncao)
print(f'Número de interações: {len(interacoesPrimeiraFuncao)}')
raizSegundaFuncao, interacoesSegundafuncao = bissecao(functions.segundaFuncao, 0, 1)
print(raizSegundaFuncao)
print(f'Número de interações: {len(interacoesSegundafuncao)}')
raizTerceiraFuncao, interacoesTerceiraFuncao = bissecao(functions.terceiraFuncao, 1, 2)
print(raizTerceiraFuncao)
print(f'Número de interações: {len(interacoesTerceiraFuncao)}')
raizQuartaFuncao, interacoesQuartaFuncao = bissecao(functions.quartaFuncao, 0, 1)
print(raizQuartaFuncao)
print(f'Número de interações: {len(interacoesQuartaFuncao)}')

gerar_csv.gerar_csv('bisection_point_1', interacoesPrimeiraFuncao)
gerar_csv.gerar_csv('bisection_point_2', interacoesSegundafuncao)
gerar_csv.gerar_csv('bisection_point_3', interacoesTerceiraFuncao)
gerar_csv.gerar_csv('bisection_point_4', interacoesQuartaFuncao)