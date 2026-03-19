'''Crie um programa que receba um valor em Reais (R$) e a cotação atual do Dólar. O programa deve exibir quanto esse valor representa em Dólares (US$).
Entrada: Valor em reais e cotação do dólar.
Processamento: dolar = reais / cotacao.
Saída: Valor convertido.'''
# 1 dólar = 5,25 reais

Val_Real = float(input("Digite o valor em Reais: ").replace(",", "."))
Cota_Dolar = float(input("Digite a cotação do dólar atual: ").replace(",", "."))

Val_Dolar = Val_Real / Cota_Dolar

print("O valor em dólares é: $" + str(Val_Dolar))




