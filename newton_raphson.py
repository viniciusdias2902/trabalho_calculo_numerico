import exibir_chutes
import functions
import gerar_csv

def newton_raphson(f, df, x0, tol=1e-6, max_iter=25):
    interacoes = []
    x = x0
    for _ in range(max_iter):
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

    for interacao in lista_interacoes:
        exibir_chutes(interacao, 'Método numérico: newton-raphson')