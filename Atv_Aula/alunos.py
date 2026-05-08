def qtd_alunos():
    print('---Quantidade de Alunos---')
    qtde = 0
    while qtde < 1:
        qtde = int(input('Quantidade de alunos: '))
        if qtde < 1:
            print('Tem que ser maior do que zero.')
        else:
            return qtde
        
def rec_notas(qtde):
    print('---Preenchendo as notas...---')
    notas = []
    for i in range(qtde):
        nota = float(input(f'Nota do aluno {i+1}: ').replace(",","."))
        notas.append(nota)
    return notas

def imprimir_notas(notas):
    print('---Notas dos Alunos---')
    for i, nota in enumerate(notas):
        print(f'Aluno {i+1}: {nota:.2f}')

def media(notas):
    print('---Média dos Alunos---')
    media = sum(notas) / len(notas)
    print(f'Média: {media:.2f}')

def reprovados(notas):
    print('---Alunos Reprovados---')
    reprovados = [nota for nota in notas if nota < 6.0]
    if reprovados:
        for i, nota in enumerate(reprovados):
            print(f'Aluno {i+1}: {nota:.2f}')
    else:
        print('Nenhum aluno reprovado.')

def main():
    qtde = qtd_alunos()
    notas = rec_notas(qtde)
    imprimir_notas(notas)
    media(notas)
    reprovados(notas)
main()



