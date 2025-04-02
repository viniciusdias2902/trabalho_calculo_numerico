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
    print(raizPrimeiraFuncao)
    print(f'Número de interações: {len(interacoesPrimeiraFuncao)}')
    raizSegundaFuncao, interacoesSegundafuncao = newton_raphson(functions.segundaFuncao, functions.derivadaSegundaFuncao, 0.5)
    print(raizSegundaFuncao)
    print(f'Número de interações: {len(interacoesSegundafuncao)}')
    raizTerceiraFuncao, interacoesTerceiraFuncao = newton_raphson(functions.terceiraFuncao, functions.derivadaTerceiraFuncao, 1.5)
    print(raizTerceiraFuncao)
    print(f'Número de interações: {len(interacoesTerceiraFuncao)}')
    raizQuartaFuncao, interacoesQuartaFuncao = newton_raphson(functions.quartaFuncao, functions.derivadaQuartaFuncao, 0.5)
    print(raizQuartaFuncao)
    print(f'Número de interações: {len(interacoesQuartaFuncao)}')

    gerar_csv.gerar_csv('newton_raphson_1', interacoesPrimeiraFuncao)
    gerar_csv.gerar_csv('newton_raphson_2', interacoesSegundafuncao)
    gerar_csv.gerar_csv('newton_raphson_3', interacoesTerceiraFuncao)
    gerar_csv.gerar_csv('newton_raphson_4', interacoesQuartaFuncao)