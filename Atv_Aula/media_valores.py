soma = 0
contador = 0

while True:
    num = float(input('Digite um número (-1 para parar): '))

    if num != -1:
        soma += num
        contador += 1
    else:
        if contador > 0:
            media = soma / contador
            print(f'Média: {media:.2f}')
        else:
            print('Nenhum número foi digitado.')
        break


