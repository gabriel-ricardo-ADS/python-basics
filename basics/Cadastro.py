usuarios = []

def cadastro():
    print("\n--- CADASTRO ---")
    nome = input("Digite o seu nome: ")
    cpf = input("Digite o seu CPF: ")
    email = input("Digite o seu email: ")
    senha = input("Digite a sua senha: ")

    if nome == "" or cpf == "" or email == "" or senha == "":
        print("Preencha todos os campos.")
        return

    # verifica se já existe
    for usuario in usuarios:
        if usuario["email"] == email:
            print("Email já cadastrado.")
            return

    # salva o usuário
    usuario = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "senha": senha,
        "saldo": 0
    }

    usuarios.append(usuario)
    print(f"Cadastro realizado com sucesso! Bem-vindo, {nome}!")


def login():
    print("\n--- LOGIN ---")

    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado ainda.")
        return

    email_login = input("Digite o seu email: ")
    senha_login = input("Digite a sua senha: ")

    if email_login == "" or senha_login == "":
        print("Preencha todos os campos.")
        return

    usuario_encontrado = None

    for usuario in usuarios:
        if usuario["email"] == email_login:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        print("Usuário não encontrado. Faça o cadastro primeiro.")
    elif usuario_encontrado["senha"] != senha_login:
        print("Senha incorreta.")
    else:
        print(f"Login realizado com sucesso! Bem-vindo de volta, {usuario_encontrado['nome']}!")
        menu_usuario(usuario_encontrado)


def menu_usuario(usuario):
    while True:
        print(f"\n--- MENU DO USUÁRIO ({usuario['nome']}) ---")
        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Seu saldo é: R$ {usuario['saldo']:.2f}")

        elif opcao == "2":
            valor = float(input("Digite o valor para depósito: "))
            usuario["saldo"] += valor
            print("Depósito realizado!")

        elif opcao == "3":
            valor = float(input("Digite o valor para saque: "))
            if valor > usuario["saldo"]:
                print("Saldo insuficiente.")
            else:
                usuario["saldo"] -= valor
                print("Saque realizado!")

        elif opcao == "4":
            print("Saindo da conta...")
            break

        else:
            print("Opção inválida.")


# MENU PRINCIPAL
while True:
    print("\n--- BEM VINDO AO SOUL ---")
    print("1 - Login")
    print("2 - Cadastro")
    print("3 - Sair")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        login()
    elif opcao == "2":
        cadastro()
    elif opcao == "3":
        print("Até mais!")
        break
    else:
        print("Opção inválida.")
