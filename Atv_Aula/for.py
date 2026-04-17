

inicio = int(input('Início: '))
fim = int(input('Fim: '))
contador = 0  
if inicio < fim:
    for n in range(inicio, fim + 1):
        if n % 2 == 0:
            print(n)
            contador += 1 
    print(f"Foram: {contador} números pares.")

elif inicio > fim:
    for n in range(inicio, fim - 1, -1):
        if n % 2 != 0: 
            print(n)
            contador += 1 
    print(f"Foram: {contador} números ímpares.")

else:
    print("Os números são iguais.")