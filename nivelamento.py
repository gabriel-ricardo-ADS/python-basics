#valor = input("digite um valor: R$")
#valor = float(valor)

#porc = input("digite a porcentagem: ")
#porc = float(porc)

#perc = valor * porc / 100
#acresc = valor + perc
#desc = valor - perc

#print("percentual: R$" + str(perc))
#print("acrescimo: R$" + str(acresc))
#print("desconto: R$" + str(desc))




#venda = float(input("digite o valor da venda: R$"))

#if venda > 300:
    #desconto = venda * 0.10
    #venda = venda - desconto

#print("valor da venda: R$", venda)


salario = float(input("digite o valor do salario: R$"))
tempo = int(input("digite o tempo de serviço: "))

if tempo < 3:
    salario = salario * 1.05
elif tempo <= 5:
    salario = salario * 1.10
elif tempo <= 10:
    salario = salario * 1.15

print("salario atualizado: R$", salario)

        

