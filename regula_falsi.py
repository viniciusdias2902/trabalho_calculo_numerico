from exibir_chutes import exibir_chutes
import functions
from gerar_csv import gerar_csv

functions.primeiraFuncao(2)

def regula_falsi(f, a , b, max_iter=100, tol=1e-6):
    interacoes = []

    if f(a) * f(b) >= 0:
        print("O produto entre f(a) e f(b) deve ser negativo \n")
        return -1
    
    c = a 
    
    for i in range(max_iter+1):
        
        c = (a * f(b) - b * f(a))/ (f(b) - f(a))
        interacoes.append(c)
        
        if abs(f(c)) < tol:
            break
        
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c, interacoes

if __name__ == "__main__":

    raizPrimeiraFuncao, interacoesPrimeiraFuncao = regula_falsi(functions.primeiraFuncao, 2, 3)
    raizSegundaFuncao, interacoesSegundafuncao = regula_falsi(functions.segundaFuncao, 0, 1)
    raizTerceiraFuncao, interacoesTerceiraFuncao = regula_falsi(functions.terceiraFuncao, 1, 2)
    raizQuartaFuncao, interacoesQuartaFuncao = regula_falsi(functions.quartaFuncao, 0, 1)

    lista_interacoes = [interacoesPrimeiraFuncao, interacoesSegundafuncao, interacoesTerceiraFuncao, interacoesQuartaFuncao]

    for index, interacao in enumerate(lista_interacoes):
        gerar_csv(f'regula_falsi_{index+1}', interacao)
        exibir_chutes(interacao, 'Método numérico: falsa posição', interacao[-1])
    