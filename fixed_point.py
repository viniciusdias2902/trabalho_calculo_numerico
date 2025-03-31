import functions
import gerar_csv

def ponto_fixo(g, x0, tol=1e-6, max_iter=25):
    interacoes = []
    for i in range(max_iter):
        x1 = g(x0)
        interacoes.append(x1)
        erro = abs(x1 - x0)
        
        
        if erro < tol:
            return x1, interacoes
        x0 = x1
    
    print("O método não convergiu após o número máximo de iterações.")
    return x1, interacoes

raizPrimeiraFuncao, interacoesPrimeiraFuncao = ponto_fixo(functions.primeiraFuncaoInteracao, 2.5)
print(raizPrimeiraFuncao)
print(f'Número de interações: {len(interacoesPrimeiraFuncao)}')
raizSegundaFuncao, interacoesSegundafuncao = ponto_fixo(functions.segundaFuncaoInteracao, 0.5)
print(raizSegundaFuncao)
print(f'Número de interações: {len(interacoesSegundafuncao)}')
raizTerceiraFuncao, interacoesTerceiraFuncao = ponto_fixo(functions.terceiraFuncaoInteracao, 1.5)
print(raizTerceiraFuncao)
print(f'Número de interações: {len(interacoesTerceiraFuncao)}')
raizQuartaFuncao, interacoesQuartaFuncao = ponto_fixo(functions.quartaFuncaoInteracao, 0.5)
print(raizQuartaFuncao)
print(f'Número de interações: {len(interacoesQuartaFuncao)}')

gerar_csv.gerar_csv('fixed_point_1', interacoesPrimeiraFuncao)
gerar_csv.gerar_csv('fixed_point_2', interacoesSegundafuncao)
gerar_csv.gerar_csv('fixed_point_3', interacoesTerceiraFuncao)
gerar_csv.gerar_csv('fixed_point_4', interacoesQuartaFuncao)