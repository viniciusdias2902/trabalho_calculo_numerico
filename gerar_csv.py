import csv


def gerar_csv(nome_metodo, lista):
    nome_arquivo = nome_metodo+'.csv'
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
    
        escritor.writerow(['Interação', 'Resultado'])
    
        for indice, elemento in enumerate(lista):
            escritor.writerow([indice+1, elemento])
