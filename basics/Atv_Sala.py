
id_vendedor = input('Digite seu Id: ') 
codigo_peca = input('Digite o código da peça: ')
valor_peca = float(input('Digite o valor da peça: '))
quantidade_vendida = int(input('Digite quantas unidades foram vendidas: '))
valor_total = valor_peca * quantidade_vendida
comissao = valor_total * 0.05

print('\n--- Resultados: ---')
print(f'Parabéns!! Vendedor: {id_vendedor}')
print(f'Código da peça: {codigo_peca}')
print(f'Total da venda: R$ {valor_total:.2f}')
print(f'Sua comissão (5%) é: R$ {comissao:.2f}')