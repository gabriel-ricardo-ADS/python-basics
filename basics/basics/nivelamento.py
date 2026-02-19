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


#salario = float(input("digite o valor do salario: R$"))
#tempo = int(input("digite o tempo de serviço: "))

#if tempo < 3:
    #salario = salario * 1.05
#elif tempo <= 5:
    #salario = salario * 1.10
#elif tempo <= 10:
    #salario = salario * 1.15

#print("salario atualizado: R$", salario)


#exemplo de imposto de renda:

salario = float(input("valor do salario: R$"))
if salario <= 1903.98:
    ir = 0
elif salario <= 2826.65:
    ir = salario * 0.075 - 142.80
elif salario <= 3751.05:
    ir = salario * 0.15 - 354.80
elif salario <= 4664.68:
    ir = salario * 0.225 - 636.13
else:
    ir = salario * 0.275 - 869.36

salario_liquido = salario - ir

print("salario liquido: R$", salario_liquido)

        
     






