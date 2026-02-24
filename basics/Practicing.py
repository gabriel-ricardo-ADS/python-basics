# ==============================
# VALIDAÇÃO DO ANO ESCOLAR
# ==============================

while True:
    try:
        ano_escolar = int(input("Ano escolar que vai cursar (digite um número): "))

        if ano_escolar in [1, 2, 3, 5, 6, 7, 8, 9]:
            print("Ano válido!")
            break
        else:
            print("Erro, digite um ano válido.")

    except ValueError:
        print("Erro, digite apenas números.")

print("\n")

# ==============================
# NOTAS
# ==============================

def ler_nota(materia):
    while True:
        try:
            nota = input(f"Digite a nota de {materia}: ").replace(",", ".")
            nota = float(nota)

            if 0 <= nota <= 10:
                return nota
            else:
                print("Digite uma nota entre 0 e 10.")

        except ValueError:
            print("Digite um número válido.")

print("Cálculo da média de notas:\n")

# ==============================
# ENTRADA DAS NOTAS
# ==============================

nota_port = ler_nota("Português")
nota_mat = ler_nota("Matemática")
nota_hist = ler_nota("História")
nota_geo = ler_nota("Geografia")
nota_quim = ler_nota("Química")
nota_fis = ler_nota("Física")
nota_bio = ler_nota("Biologia")
nota_ef = ler_nota("Educação Física")

# ==============================
# CÁLCULO DA MÉDIA (ponderada)
# ==============================

media_notas = (
    nota_port * 2 +
    nota_mat * 2 +
    nota_hist +
    nota_geo +
    nota_quim * 3 +
    nota_fis * 3 +
    nota_bio * 3 +
    nota_ef
) / 16

print(f"\nMédia final: {media_notas:.2f}")

# ==============================
# VERIFICA APROVAÇÃO
# ==============================

if media_notas < 6:
    print("Reprovado.")
    input("Pressione Enter para sair...")
    exit()

print("Aprovado!")

print("\n")

# ==============================
# DEFINIÇÃO DA MENSALIDADE BASE
# ==============================

if ano_escolar in [5, 6, 7]:
    mensalidade = 1500
elif ano_escolar in [8, 9]:
    mensalidade = 1600
else:  # 1, 2, 3
    mensalidade = 2000

# ==============================
# CÁLCULO DA BOLSA
# ==============================

if media_notas == 10:
    desconto = 0.30
elif media_notas >= 9:
    desconto = 0.20
elif media_notas >= 8:
    desconto = 0.10
else:
    desconto = 0

valor_final = mensalidade * (1 - desconto)

# ==============================
# RESULTADO FINAL
# ==============================

if desconto > 0:
    print(f"Parabéns! Você ganhou bolsa de {int(desconto*100)}%.")
else:
    print("Infelizmente, sem bolsa de estudos.")

print(f"Valor da mensalidade: R$ {valor_final:.2f}")

input("\nPressione Enter para sair...")


    



