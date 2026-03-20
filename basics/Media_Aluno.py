while True:

    #Identificação do aluno
    print("----------IDENTIDADE---------")
    nome = input("Digite seu nome: ")
    rm = input("Digite seu Rm: ")
    email = input("Digite seu email: ")

    # input das notas das matérias 
    print("----------NOTAS----------")
    notaPython = float(input('Nota de Python: ').replace(",","."))
    notaJava = float(input('Nota de Java: ').replace(",","."))
    notaFront = float(input('Nota de Front End: ').replace(",","."))
    notaEng = float(input('Nota de Engenharia de Software: ').replace(",","."))
    notaData = float(input('Nota de Database: ').replace(",","."))
    notaIA = float(input('Nota de IA: ').replace(",","."))

    print("---------FALTAS---------")
    faltas = float(input("Digite quantas faltas você possui no semestre: "))

    notas_Aluno = {
        'Python': notaPython, 
        'Java': notaJava, 
        'Front End': notaFront, 
        'Eng Soft': notaEng, 
        'Database': notaData,
        'IA': notaIA,
    }
        
    # calculo da média
    media_notas = sum(notas_Aluno.values()) / len(notas_Aluno)

    print('----------MÉDIA----------')
    print(f"Media do Aluno Rm{rm}: {media_notas:.2f}")

    print('----------SITUACAO----------')

    if faltas > 18:
        print(f'O aluno RM{rm} está Reprovado!')
        break

    if media_notas < 6:
        print(f'Encaminhado para o Exame Final!')
        exame = float(input("Digite sua nota no exame final!"))

        if exame < 6:
            print(f'O aluno RM{rm} está Reprovado!')
        else:
            print(f'O Aluno RM{rm} está Aprovado!!')
        break

    else:
        print(f'O Aluno RM{rm} está Aprovado!!')
        break

input('\naperte ENTER para sair')   