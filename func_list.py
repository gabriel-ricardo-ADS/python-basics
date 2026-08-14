print('---CRIAÇÃO DA MATRIZ---')
n_linhas = int(input('Quantas linhas?: '))
n_colunas = int(input('Quantas colunas?: '))

def criar_matriz(n_linhas, n_colunas):
    matriz = []
    
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            posicao = float(input(f'Digite o elemento da posição [{i+1}][{j+1}]: ')) 
            linha.append(posicao)
        matriz.append(linha)    
    return matriz 

def mostrar_matriz(matriz):
    print('\n---MATRIZ---')
    for linha in matriz:
        print(linha)

def imprimir_elemento(matriz):
    print('\n---ELEMENTOS INDIVIDUAIS---')
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'Elemento [{i+1}][{j+1}]: {matriz[i][j]}')

n_matriz = criar_matriz(n_linhas, n_colunas)
mostrar_matriz(n_matriz)
imprimir_elemento(n_matriz) 
