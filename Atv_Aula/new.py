num = int(input('Digite o número (1; 2; 3): '))

match num:
    case 1:
        print(f'O usuário digitou {num}')
    case 2:
        print(f'O usuário digitou {num}')
    case 3:
        print(f'O usuário digitou {num}')
    case _:
        print(f'Número Inválido')

status = input('Status do envio: ').lower()

match status:
    case 'pendente':
        print('Aguardando Pagamento')
    case 'pago':
        print("Preparando para envio")
    case 'enviado':
        print('Produto a caminho!')
    case 'entregue':
        print('Pedido Finalizado')
    case _:
        print(f'Status {status} nao reconhecido')