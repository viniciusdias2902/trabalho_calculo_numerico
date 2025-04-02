from exibir_chutes import exibir_chutes
import functions

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
    raizSegundaFuncao, interacoesSegundafuncao = regula_falsi(functions.segundaFuncao, 0, 1)
    raizTerceiraFuncao, interacoesTerceiraFuncao = regula_falsi(functions.terceiraFuncao, 1, 2)
    raizQuartaFuncao, interacoesQuartaFuncao = regula_falsi(functions.quartaFuncao, 0, 1)

    lista_interacoes = [interacoesPrimeiraFuncao, interacoesSegundafuncao, interacoesTerceiraFuncao, interacoesQuartaFuncao]

    for interacao in lista_interacoes:
        exibir_chutes(interacao, 'Método numérico: falsa posição')
