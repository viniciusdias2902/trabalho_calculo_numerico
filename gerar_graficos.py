import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PASTAS_METODOS = ['bisection', 'fixed_point', 'newton_raphson', 'regula_falsi', 'secant']
NUM_FUNCOES = 4
CORES = sns.color_palette('husl', n_colors=5)

def carregar_dados():
    dados = {f: [] for f in range(1, NUM_FUNCOES+1)}
    
    for metodo in PASTAS_METODOS:
        for funcao in range(1, NUM_FUNCOES+1):
            caminho = os.path.join(metodo, f'{metodo}_{funcao}.csv')
            df = pd.read_csv(caminho)
            df['Método'] = metodo.capitalize()
            dados[funcao].append(df)
    
    return dados

def plotar_convergencia_individual(dados):
    """Gráficos individuais para cada função com todos os métodos"""
    for funcao, dfs in dados.items():
        plt.figure(figsize=(12, 7))
        plt.title(f'Convergência dos Métodos - Função {funcao}', fontsize=14)
        
        for idx, df in enumerate(dfs):
            metodo = df['Método'].iloc[0]
            plt.plot(df['Interação'], df['Resultado'], 
                    marker='o', 
                    linewidth=1.5,
                    markersize=4,
                    color=CORES[idx],
                    label=f'{metodo} ({len(df)} iterações)')
        
        plt.xlabel('Iteração', fontsize=12)
        plt.ylabel('Aproximação da Raiz', fontsize=12)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'convergencia_funcao_{funcao}.png', dpi=300)
        plt.close()

def plotar_comparacao_desempenho(dados):
    """Gráfico comparativo de desempenho entre métodos"""
    desempenho = []
    
    for funcao, dfs in dados.items():
        for df in dfs:
            metodo = df['Método'].iloc[0]
            desempenho.append({
                'Função': funcao,
                'Método': metodo,
                'Iterações': len(df)
            })
    
    df_desempenho = pd.DataFrame(desempenho)
    
    plt.figure(figsize=(14, 8))
    sns.barplot(x='Função', y='Iterações', hue='Método', 
                data=df_desempenho, palette=CORES)
    plt.title('Comparação de Desempenho entre Métodos', fontsize=14)
    plt.xlabel('Função Testada', fontsize=12)
    plt.ylabel('Iterações Necessárias', fontsize=12)
    plt.legend(title='Método')
    plt.tight_layout()
    plt.savefig('comparacao_desempenho.png', dpi=300)
    plt.close()

def gerar_relatorio(dados):
    analise = []
    
    for funcao, dfs in dados.items():
        melhor_metodo = min(dfs, key=lambda x: len(x))
        analise.append({
            'Função': funcao,
            'Melhor Método': melhor_metodo['Método'].iloc[0],
            'Iterações': len(melhor_metodo),
            'Convergência Final': melhor_metodo['valor'].iloc[-1]
        })
    
    df_analise = pd.DataFrame(analise)
    print("Relatório de Análise:\n")
    print(df_analise.to_string(index=False))

def main():
    sns.set_theme(style="whitegrid")
    plt.rcParams['font.family'] = 'DejaVu Sans'
    
    dados = carregar_dados()
    
    plotar_convergencia_individual(dados)
    plotar_comparacao_desempenho(dados)
    
    gerar_relatorio(dados)

if __name__ == "__main__":
    main()
