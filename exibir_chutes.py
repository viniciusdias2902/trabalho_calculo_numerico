def exibir_chutes(chutes, metodo, precisao=10):
    largura_iter = 12
    largura_chute = 25
    largura_erro = 25
    
    print("─" * (largura_iter + largura_chute + largura_erro + 2))
    print(f"{metodo.upper():^{largura_iter + largura_chute + largura_erro + 2}}")
    print("─" * (largura_iter + largura_chute + largura_erro + 2))
    print(f"{'Iteração':^{largura_iter}}│{'Chute':^{largura_chute}}│{'Erro Relativo (%)':^{largura_erro}}")
    print("─" * (largura_iter + largura_chute + largura_erro + 2))

    for i, x in enumerate(chutes):
        erro = abs((chutes[i] - chutes[i-1])/chutes[i])*100 if i > 0 else 0
        erro_str = f"{erro:.4e}" if i > 0 else "─"
        
        print(f"{i:^{largura_iter}}│{x:^{largura_chute}.{precisao}f}│{erro_str:^{largura_erro}}")

    print("─" * (largura_iter + largura_chute + largura_erro + 2))
