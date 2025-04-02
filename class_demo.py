from exibir_chutes import exibir_chutes
from regula_falsi import regula_falsi
from fixed_point import ponto_fixo
from newton_raphson import newton_raphson
from bisection import bissecao
import functions



raizPrimeiraFuncao, interacoesPrimeiraFuncao = regula_falsi(functions.primeiraFuncao, 2, 3)
exibir_chutes(interacoesPrimeiraFuncao, 'Método numérico: posição Falsa')
raizSegundaFuncao, interacoesSegundaFuncao = ponto_fixo(functions.segundaFuncaoInteracao, 0.5)
exibir_chutes(interacoesSegundaFuncao, 'Método numérico: ponto fixo')
raizTerceiraFuncao, interacoesTerceiraFuncao = newton_raphson(functions.terceiraFuncao, functions.derivadaTerceiraFuncao, 1.5)
exibir_chutes(interacoesTerceiraFuncao, 'Método numérico: newton-raphson')
raizQuartaFuncao, interacoesQuartaFuncao = bissecao(functions.quartaFuncao, 0, 1)
exibir_chutes(interacoesQuartaFuncao, 'Método numérico: bisseção')
