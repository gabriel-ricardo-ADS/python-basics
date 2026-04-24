'''
escreva um programa que leia 5 nomes e armazene em uma lista
'''
nomes = []

for i in range(5):
    nome = input(f'Digite o {i+1}º nome: ')
    nomes.append(nome)

print('\n--- Nomes ---')
for nome in nomes:
    print(nome.capitalize())

print('\n--- Nomes que iniciam com vogal ---')

cont_vogal = 0
for n in nomes:
    if n[0].lower() in 'aeiou':
        cont_vogal += 1
        print(n.capitalize())

cont_total = len(nomes)
cont_cons = cont_total - cont_vogal

print(f'\nSão {cont_vogal} nomes com vogal')
print(f'Sobram {cont_cons} nomes com consoante')



     







    