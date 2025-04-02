def exibir_chutes(chutes, metodo, precisao=10):
 
    BOLD = '\033[1m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'
    LINE = f"{BOLD}{CYAN}│{RESET}"
    
    print(f"\n{BOLD}{BLUE}┌{'─' * 62}┐{RESET}")
    print(f"{BOLD}{BLUE}│ {GREEN}● {MAGENTA}{metodo.upper():^58} {BLUE}●{RESET} {BOLD}{BLUE}│{RESET}")
    print(f"{BOLD}{BLUE}├{'─' * 29}┬{'─' * 31}┤{RESET}")
    print(f"{BOLD}{BLUE}│ {YELLOW}Iteração {LINE} {YELLOW}Chute{' ' * (precisao + 2)} {LINE} {YELLOW}Erro Relativo (%) {RESET}{BOLD}{BLUE}│{RESET}")
    print(f"{BOLD}{BLUE}├{'─' * 29}┼{'─' * 31}┤{RESET}")

    for i, x in enumerate(chutes):
        erro = abs((chutes[i] - chutes[i-1])/chutes[i])*100 if i > 0 else 0
        col_iter = f"{i:03d}"
        col_chute = f"{x:.{precisao}f}"
        col_erro = f"{erro:.4e}" if i > 0 else "─"
        
        print(f"{BOLD}{BLUE}│ {CYAN}{col_iter:^8} {LINE} {YELLOW}{col_chute:^{precisao + 6}} "
              f"{LINE} {GREEN}{col_erro:^15} {BOLD}{BLUE}│{RESET}")

    print(f"{BOLD}{BLUE}└{'─' * 29}┴{'─' * 31}┘{RESET}")
    print(f"{BOLD}{MAGENTA}Último chute: {YELLOW}{chutes[-1]:.{precisao}f}{RESET}\n")