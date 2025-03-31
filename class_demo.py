import functions
import regula_falsi
import fixed_point
import secant
import bisection

raizPrimeiraFuncao, interacoesPrimeiraFuncao = regula_falsi.regula_falsi(functions.primeiraFuncao, 2, 3)
print(raizPrimeiraFuncao)
print(f'Número de interações: {len(interacoesPrimeiraFuncao)}')
raizSegundaFuncao, interacoesSegundaFuncao = fixed_point.ponto_fixo(functions.segundaFuncaoInteracao, 0.5)
print(raizSegundaFuncao)
print(f'Número de interações: {len(interacoesSegundaFuncao)}')
raizTerceiraFuncao, interacoesTerceiraFuncao = secant.secante(functions.terceiraFuncao, 1, 2)
print(raizTerceiraFuncao)
print(f'Número de interações: {len(interacoesTerceiraFuncao)}')
raizQuartaFuncao, interacoesQuartaFuncao = bisection.bissecao(functions.quartaFuncao, 0, 1)
print(raizQuartaFuncao)
print(f'Número de interações: {len(interacoesQuartaFuncao)}')