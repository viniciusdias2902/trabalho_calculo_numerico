import functions
import gerar_csv

functions.primeiraFuncao(2)

def regula_falsi(f, a , b, max_iter=25):
    interacoes = []

    if f(a) * f(b) >= 0:
        print("O produto entre f(a) e f(b) deve ser negativo \n")
        return -1
    
    c = a 
    
    for i in range(max_iter):
        
        c = (a * f(b) - b * f(a))/ (f(b) - f(a))
        interacoes.append(c)
        
        if f(c) == 0:
            break
        
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c, interacoes

if __name__ == "__main__":

    raizPrimeiraFuncao, interacoesPrimeiraFuncao = regula_falsi(functions.primeiraFuncao, 2, 3)
    print(raizPrimeiraFuncao)
    print(f'Número de interações: {len(interacoesPrimeiraFuncao)}')
    raizSegundaFuncao, interacoesSegundafuncao = regula_falsi(functions.segundaFuncao, 0, 1)
    print(raizSegundaFuncao)
    print(f'Número de interações: {len(interacoesSegundafuncao)}')
    raizTerceiraFuncao, interacoesTerceiraFuncao = regula_falsi(functions.terceiraFuncao, 1, 2)
    print(raizTerceiraFuncao)
    print(f'Número de interações: {len(interacoesTerceiraFuncao)}')
    raizQuartaFuncao, interacoesQuartaFuncao = regula_falsi(functions.quartaFuncao, 0, 1)
    print(raizQuartaFuncao)
    print(f'Número de interações: {len(interacoesQuartaFuncao)}')

    gerar_csv.gerar_csv('regula_falsi_point_1', interacoesPrimeiraFuncao)
    gerar_csv.gerar_csv('regula_falsi_point_2', interacoesSegundafuncao)
    gerar_csv.gerar_csv('regula_falsi_point_3', interacoesTerceiraFuncao)
    gerar_csv.gerar_csv('regula_falsi_point_4', interacoesQuartaFuncao)