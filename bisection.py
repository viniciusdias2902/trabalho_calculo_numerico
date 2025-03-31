import functions
import gerar_csv

functions.primeiraFuncao(2)

def bissecao(f, a, b, tol=1e4, max_iter=25):
    resultados = []
    if f(a) * f(b) >= 0:
        print("O método da bisseção requer que f(a) e f(b) tenham sinais opostos.")
        return None
    
    c_anterior = None

    interacao = 0
    while interacao < (max_iter):
        c = (a + b) / 2            
        resultados.append(c)
        if abs(f(c)) <= tol or (b - a)  <= tol or  c_anterior is not None and abs(c - c_anterior) < tol:
            return c, resultados
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c_anterior = c
        interacao+=1
    
    print("O método não convergiu após o número máximo de iterações.")
    return None


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