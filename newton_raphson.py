import exibir_chutes
import functions
from gerar_csv import gerar_csv

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    interacoes = []
    x = x0
    for _ in range(max_iter+1):
        fx = f(x)
        if abs(fx) < tol:
            return x, interacoes
        
        dfx = df(x)
        if dfx == 0:
            print("Derivada zero. Método não converge.")
            return x, interacoes
            
        x -= fx / dfx
        interacoes.append(x)
    
    print("Não convergiu após {} iterações".format(max_iter))
    return x, interacoes


if __name__ == "__main__":

    raizPrimeiraFuncao, interacoesPrimeiraFuncao = newton_raphson(functions.primeiraFuncao, functions.derivadaPrimeiraFuncao, 2.5)
    raizSegundaFuncao, interacoesSegundafuncao = newton_raphson(functions.segundaFuncao, functions.derivadaSegundaFuncao, 0.5)
    raizTerceiraFuncao, interacoesTerceiraFuncao = newton_raphson(functions.terceiraFuncao, functions.derivadaTerceiraFuncao, 1.5)
    raizQuartaFuncao, interacoesQuartaFuncao = newton_raphson(functions.quartaFuncao, functions.derivadaQuartaFuncao, 0.5)

    lista_interacoes = [interacoesPrimeiraFuncao, interacoesSegundafuncao, interacoesTerceiraFuncao, interacoesQuartaFuncao]

    for index, interacao in enumerate(lista_interacoes):
        gerar_csv(f'newton_raphson{index+1}', interacao)
        exibir_chutes(interacao, 'Método numérico: newton-raphson')
    
    gerar_csv('newton_raphson', interacoesPrimeiraFuncao)
    gerar_csv('newton_raphson', interacoesSegundafuncao)
    gerar_csv('newton_raphson', interacoesTerceiraFuncao)
    gerar_csv('newton_raphson', interacoesQuartaFuncao)