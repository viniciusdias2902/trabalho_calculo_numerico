from exibir_chutes import exibir_chutes
import functions
from gerar_csv import gerar_csv

def secante(f, x0, x1, tol=1e-6, max_iter=100):
    interacoes = []
    for _ in range(max_iter+1):
        if abs(f(x1) - f(x0)) < 1e-12:  # Evita divisão por zero
            print("Erro: Divisão por zero")
            return None
        
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        interacoes.append(x2)
        if abs(x2 - x1) < tol:
            return x2, interacoes
        
        # Atualiza os pontos
        x0, x1 = x1, x2

if __name__ == "__main__":


    raizPrimeiraFuncao, interacoesPrimeiraFuncao = secante(functions.primeiraFuncao, 2, 3)
    raizSegundaFuncao, interacoesSegundafuncao = secante(functions.segundaFuncao, 0, 1)
    raizTerceiraFuncao, interacoesTerceiraFuncao = secante(functions.terceiraFuncao, 1, 2)
    raizQuartaFuncao, interacoesQuartaFuncao = secante(functions.quartaFuncao, 0, 1)
    lista_interacoes = [interacoesPrimeiraFuncao, interacoesSegundafuncao, interacoesTerceiraFuncao, interacoesQuartaFuncao]


    for interacao in lista_interacoes:
        exibir_chutes(interacao, 'Método numérico: secante')

    gerar_csv('secant', interacoesPrimeiraFuncao)
    gerar_csv('secant', interacoesSegundafuncao)
    gerar_csv('secant', interacoesTerceiraFuncao)
    gerar_csv('secant', interacoesQuartaFuncao)