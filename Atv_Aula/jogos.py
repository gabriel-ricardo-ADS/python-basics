jogos = []

def jogos_iniciais(nome, jogos):
    for i in range(5):
        nome = input(f"Digite o nome do jogo {i+1}: ").upper()
        jogos.append(nome)

def adicionar_remover_jogo(conf, novo_jogo, remover_jogo):
    while True:    
        conf = input("\nDeseja adicionar ou remover um jogo? (AD/REM/N): ").upper()
        if conf == "N":
                print("\n---Lista final ordenada---")
                jogos.sort()
                print(jogos)
                break 
        if conf == "AD":
            novo_jogo = input("\nDigite o nome do novo jogo: ").upper()
            jogos.append(novo_jogo)
            print("\n---Lista atualizada ---")
            print(jogos)
            continue
        elif conf == "REM":    
            remover_jogo = input("\nDigite o nome do jogo a ser removido: ").upper()
            if remover_jogo in jogos:
                jogos.remove(remover_jogo)
                print("\n---Lista atualizada ---")
                print(jogos)
                continue
            else:
                print("\nJogo não encontrado na lista.")
                continue

jogos_iniciais("Jogo", jogos)
adicionar_remover_jogo(None, None, None)
