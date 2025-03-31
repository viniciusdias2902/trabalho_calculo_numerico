import functions
import gerar_csv

def secante(f, x0, x1, tol=1e-6, max_iter=25):
    interacoes = []
    for _ in range(max_iter):
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
    print(raizPrimeiraFuncao)
    print(f'Número de interações: {len(interacoesPrimeiraFuncao)}')
    raizSegundaFuncao, interacoesSegundafuncao = secante(functions.segundaFuncao, 0, 1)
    print(raizSegundaFuncao)
    print(f'Número de interações: {len(interacoesSegundafuncao)}')
    raizTerceiraFuncao, interacoesTerceiraFuncao = secante(functions.terceiraFuncao, 1, 2)
    print(raizTerceiraFuncao)
    print(f'Número de interações: {len(interacoesTerceiraFuncao)}')
    raizQuartaFuncao, interacoesQuartaFuncao = secante(functions.quartaFuncao, 0, 1)
    print(raizQuartaFuncao)
    print(f'Número de interações: {len(interacoesQuartaFuncao)}')

    gerar_csv.gerar_csv('secant_point_1', interacoesPrimeiraFuncao)
    gerar_csv.gerar_csv('secant_point_2', interacoesSegundafuncao)
    gerar_csv.gerar_csv('secant_point_3', interacoesTerceiraFuncao)
    gerar_csv.gerar_csv('secant_point_4', interacoesQuartaFuncao)