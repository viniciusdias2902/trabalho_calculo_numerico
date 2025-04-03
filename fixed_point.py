from exibir_chutes import exibir_chutes
import functions
from gerar_csv import gerar_csv

def ponto_fixo(g, x0, tol=1e-6, max_iter=100):
    interacoes = []
    for i in range(max_iter+1):
        x1 = g(x0)
        interacoes.append(x1)
        erro = abs(x1 - x0)
        
        
        if erro < tol:
            return x1, interacoes
        x0 = x1
    
    print("O método não convergiu após o número máximo de iterações.")
    return x1, interacoes

if __name__ == "__main__":

    raizPrimeiraFuncao, interacoesPrimeiraFuncao = ponto_fixo(functions.primeiraFuncaoInteracao, 2.5)
    raizSegundaFuncao, interacoesSegundafuncao = ponto_fixo(functions.segundaFuncaoInteracao, 0.5)
    raizTerceiraFuncao, interacoesTerceiraFuncao = ponto_fixo(functions.terceiraFuncaoInteracao, 1.5)
    raizQuartaFuncao, interacoesQuartaFuncao = ponto_fixo(functions.quartaFuncaoInteracao, 0.5)

    lista_interacoes = [interacoesPrimeiraFuncao, interacoesSegundafuncao, interacoesTerceiraFuncao, interacoesQuartaFuncao]

    for index, interacao in enumerate(lista_interacoes):
        gerar_csv(f'fixed_point_{index+1}', interacao)
        exibir_chutes(interacao, 'Método numérico: ponto fixo')
