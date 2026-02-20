
dia = int(input("Digite o dia da semana: "))
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("Dia inválido.")

Renda_Bruta = float(input("Digite a renda bruta da empresa: "))
salarioGerente = Renda_Bruta * 0.05
salarioSupervisor = Renda_Bruta * 0.01
salarioFuncionario = Renda_Bruta * 0.005
cargo = input("Digite o cargo na empresa: ").strip().lower()
if cargo == "ceo":
    salario = Renda_Bruta - (salarioGerente * 2 + salarioSupervisor * 10 + salarioFuncionario * 50)
elif cargo == "gerente":
    salario = salarioGerente
elif cargo == "supervisor":
    salario = salarioSupervisor
elif cargo == "funcionário":
    salario = salarioFuncionario
else:
    print("Cargo inválido.")
    salario = 0

print(f"O salário do {cargo} é: R${salario:.2f}")

valor_unitario = float(input("Digite o valor unitário do produto: "))
vendas = float(input("Digite o número de vendas efetuadas: "))
lucro = vendas * valor_unitario 
if vendas == 0:
    comissao = 0 
elif vendas <= 10:
    comissao = lucro * 0.005
elif vendas <= 20:
    comissao = lucro * 0.01
elif vendas <= 50:
    comissao = lucro * 0.015
else:
    comissao = lucro * 0.02


print(f"A comissão do vendedor é: R${comissao:.2f}")
               

    
    


    