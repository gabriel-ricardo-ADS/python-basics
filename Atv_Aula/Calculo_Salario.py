'''
Enunciado: Uma empresa paga um salário fixo de R$ 2.000,00 mais uma comissão de 15% sobre o total de vendas efetuadas pelo vendedor. Receba o total de vendas do mês e exiba o salário final.
Entrada: Total de vendas.
Processamento: total = 2000 + (vendas * 0.15).
Saída: Salário final formatado.
'''
Sal_Fixo = 2000
Vendas = float(input("Digite o total de vendas (Em R$): "))

Sal_Final = Sal_Fixo + (Vendas * 0.15)

print(f"O seu salário, calculado com a comissão, é: R${Sal_Final}")


