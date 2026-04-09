'''Exercício: Sistema de Caixa de Supermercado
 
Desenvolva um programa em Python que simule o fechamento de um caixa. O sistema deve ler o preço de cada item (valor real) de forma contínua.
Para encerrar a entrada de dados, o usuário deve digitar o valor sentinela -1.
Ao final, o programa deve exibir o valor total acumulado da compra, formatado como moeda (duas casas decimais).
Atenção: O valor sentinela não deve ser somado ao total'''

compra = 0.0

while True:
    item = float(input('Digite o valor do item (ou -1 para encerrar): R$ '))
    if item == -1:
        break
    elif item < 0:
        print('Valor inválido. Digite um valor positivo ou -1 para encerrar.')
        continue
    else:
        compra += item

print(f'Valor total da compra: R$ {compra:.2f}')