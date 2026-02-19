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




venda = float(input("digite o valor da venda: R$"))

if venda > 300:
    desconto = venda * 0.10
    venda = venda - desconto

print("valor da venda: R$", venda)


