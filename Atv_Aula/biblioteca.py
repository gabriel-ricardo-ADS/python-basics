biblioteca = []

def adicionar_livro(livro):
    livro = input("Digite o nome do livro: ").upper()
    biblioteca.append(livro)
    print(f"\nLivro '{livro}' adicionado à biblioteca.")
    return livro

def remover_livro(livro):
    livro = input("Digite o nome do livro a ser removido: ").upper()
    if livro in biblioteca:
        biblioteca.remove(livro)
        print(f"\nLivro '{livro}' removido da biblioteca.")
    else:
        print(f"\nLivro '{livro}' não encontrado na biblioteca.")
    return livro

def listar_livros(biblioteca):
    if biblioteca:
        print("\n---Lista de Livros na Biblioteca---")
        for livro in biblioteca:
            print(livro)
    else:
        print("\nA biblioteca está vazia.")
        return biblioteca

def main(acao):
    while True:
        acao = input("\nDeseja adicionar, remover ou listar livros? (AD/REM/LIST/N): ").upper()
        if acao == "N":
            print("\n---Lista final ordenada---")
            biblioteca.sort()
            break
        elif acao == "AD":
            adicionar_livro(None)
        elif acao == "REM":
            remover_livro(None)
        elif acao == "LIST":
            listar_livros(biblioteca)
        else:
            print("\nOpção inválida. Por favor, escolha AD, REM, LIST ou N.")
            return acao 

main()