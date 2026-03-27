contador = 4


senha = float(input('Crie uma senha numérica: '))

print('------INTERFACE------')
dig = float(input('Digite a Senha (4 tentativas): '))

while True:
    if dig != senha:
        contador -= 1
        print('Senha Incorreta!')
        dig = float(input(f'Digite a senha novamente ({contador} tentativas): '))
        
    else:
        print('Senha correta, Bem-vindo!')
        break

    if contador == 0:
        print('Número máximo de tentativas!')
        break
