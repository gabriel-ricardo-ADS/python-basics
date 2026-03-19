'''
Enunciado: Escreva um programa que leia a base e a altura de um retângulo e exiba sua área e seu perímetro.
Fórmulas: Area = base * altura | Perimetro = 2 * (base + altura).
'''
Base_Ret = float(input("Digite o comprimento da base do retângulo (cm): "))
Alt_Ret = float(input("Digite o valor da altura do retângulo (cm): "))

area = Base_Ret * Alt_Ret
peri = (2 * Base_Ret) + (2 * Alt_Ret)

print(f"A área do Retângulo, de perímetro {peri}cm, é de: {area}cm²")