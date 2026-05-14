
album = []

def adicionar_musica(musica):
    musica = input("Digite o nome da música: ").upper()
    album.append(musica)
    print(f"\nMúsica '{musica}' adicionada ao álbum.")
    return musica

def remover_musica(musica):
    musica = input("Digite o nome da música a ser removida: ").upper()
    if musica in album:
        album.remove(musica)
        print(f"\nMúsica '{musica}' removida do álbum.")
    else:
        print(f"\nMúsica '{musica}' não encontrada no álbum.")
    return musica

def listar_musicas(album):
    if album:
        print("\n---Lista de Músicas no Álbum---")
        for musica in album:
            print(musica)
    else:
        print("\nO álbum está vazio.")
        return album
    
def menu(acao):
    while True:
        print("\nBem vindo ao gerenciador de álbum de músicas!")
        print("Escolha uma opção:")
        print("1 - Adicionar música")
        print("2 - Remover música")
        print("3 - Listar músicas")
        print("4 - Sair")
        acao = input("Digite o número da opção desejada: ")
        if acao == "4":
            print("\n---Lista final ordenada---")
            album.sort()
            print(album)
            break
        elif acao == "1":
            adicionar_musica(None)
        elif acao == "2":
            remover_musica(None)
        elif acao == "3":
            listar_musicas(album)
        else:
            print("\nOpção inválida. Por favor, escolha 1, 2, 3 ou 4.")
            return acao
        
menu(None)