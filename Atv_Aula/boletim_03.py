def criar_matriz_notas(nomes):
    matriz = []
    for nome in nomes:
        print(f'\nNotas do(a) {nome}:')
        notas = []
        for j in range(3):
            nota = float(input(f'Digite a {j+1}° nota: '))
            notas.append(nota)
        media = sum(notas) / len(notas)
        matriz.append([notas[0], notas[1], notas[2], media])
    return matriz

def criar_lista_nomes(n):
    nomes = []
    for i in range(n):
        nome = input(f'Nome do {i+1}° aluno: ')
        nomes.append(nome)
    return nomes

def imprimir_relatorio(nomes, matriz_notas):
    print("\n" + "="*55)
    print(f"{'ALUNO':<15} | {'NOTA 1':<7} | {'NOTA 2':<7} | {'NOTA 3':<7} | {'MÉDIA':<7}")
    print("="*52)
    
    for i in range(len(nomes)):
        nome = nomes[i]
        n1, n2, n3, media = matriz_notas[i]
        print(f"{nome:<15} | {n1:<7.1f} | {n2:<7.1f} | {n3:<7.1f} | {media:<7.1f}")
        
    print("="*55)

n_alunos = int(input('Número de alunos: '))
lista_nomes = criar_lista_nomes(n_alunos)
lista_notas = criar_matriz_notas(lista_nomes)

imprimir_relatorio(lista_nomes, lista_notas)

