'''Simulação de Compras com Limite de Crédito
 
Desenvolva um programa que gerencie o limite de crédito de um cliente durante uma sessão de compras. O programa deve simular o funcionamento de uma carteira digital ou cartão pré-pago.
 
Requisitos:
Entrada de Crédito: O programa deve iniciar solicitando ao usuário o valor do Crédito Disponível (valor real).
Processamento de Itens: Utilize uma estrutura de repetição para receber o preço de cada item sucessivamente.
Lógica de Abatimento: A cada item inserido, o programa deve verificar se o saldo atual é suficiente para cobri-lo:
Se o saldo for suficiente, o valor do item é subtraído do crédito e a compra continua.
Se o saldo for insuficiente, o programa deve informar que não há crédito para aquele item e encerrar a entrada de dados imediatamente.
Saída de Dados: Ao final, exiba:
O Valor Total acumulado da compra.
O Saldo Restante (crédito que sobrou).'''

cred = float(input('Digite o valor do crédito disponível: R$ '))
tot_itens = 0.0

if cred == "":
    print('Valor de crédito inválido. Encerrando programa.')
    print(f'Gasto com compras: R${tot_itens:.2f}. Saldo restante: R$ {cred:.2f}')
    exit()

if cred < 0:
    print('Valor de crédito não pode ser negativo. Encerrando programa.')
    print(f'Gasto com compras: R${tot_itens:.2f}. Saldo restante: R$ {cred:.2f}')
    exit()

if cred == 0:
    print('Crédito insuficiente para realizar compras. Encerrando programa.')
    print(f'Gasto com compras: R${tot_itens:.2f}. Saldo restante: R$ {cred:.2f}')
    exit()

while True:
    it = float(input('Digite o valor do item: '))
    if it < 0:
        print('Valor do item não pode ser negativo. Tente novamente.')
        continue
    if it == "":
        print('Valor do item inválido. Tente novamente.')
        continue
    if it <= cred:
        cred -= it
        tot_itens += it
        print(f'Item adicionado. Saldo restante: R$ {cred:.2f}')
        if cred == 0:
            print('Crédito esgotado. Encerrando compras.')
            print(f'Gasto com compras: R${tot_itens:.2f}. Saldo restante: R$ {cred:.2f}')
            break
    elif it > cred:
        print('Crédito insuficiente para este item. Encerrando compras.')
        print(f'Gasto com compras: R${tot_itens:.2f}. Saldo restante: R$ {cred:.2f}')
        break
    cont = input('Deseja adicionar outro item? (s/n): ').lower()
    if cont == 'n':
        print('Encerrando compras.')
        print(f'Gasto com compras: R${tot_itens:.2f}. Saldo restante: R$ {cred:.2f}')
        break
    else:
        continue 

