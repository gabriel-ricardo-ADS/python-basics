'''
programa em python para resolver as notas da fiap

cp 1. 2 e 3 = 20% (uma é desconsiderada)
sprints = 20% cada (média entre as duas)
gs = 60%

primeiro semestre = 40%
segundo semestre = 60%

se tirar acima de 6 é aprovado
entre 2 e 6 fica de exame
abaixo de 2 ta reprovado (impossivel passar com o exame)
'''

print('--- CÁLCULO DE MÉDIA DO BOLETIM ---')
print('--- PRIMEIRO SEMESTRE ---')

def notas_cp(semestre):
    cp1 = float(input(f'Digite sua nota da CP1 ({semestre} semestre): '))
    cp2 = float(input(f'Digite sua nota da CP2 ({semestre} semestre): '))
    cp3 = float(input(f'Digite sua nota da CP3 ({semestre} semestre): '))
    notas = [cp1, cp2, cp3]
    return (sum(notas) - min(notas)) / 2 

def notas_sprint(semestre):
    sp1 = float(input(f'Digite sua nota da Sprint 1 ({semestre} semestre): '))
    sp2 = float(input(f'Digite sua nota da Sprint 2 ({semestre} semestre): '))
    return (sp1 + sp2) / 2

def notas_gs(semestre): 
    return float(input(f'Digite a nota da Global Solution ({semestre} semestre): '))

media_cps_s1 = notas_cp("1º")
media_sprints_s1 = notas_sprint("1º")
gs_s1 = notas_gs("1º")

media_s1 = (media_cps_s1 * 0.20) + (media_sprints_s1 * 0.20) + (gs_s1 * 0.60)


print('\n--- SEGUNDO SEMESTRE ---')

media_cps_s2 = notas_cp("2º")
media_sprints_s2 = notas_sprint("2º")
gs_s2 = notas_gs("2º")

media_s2 = (media_cps_s2 * 0.20) + (media_sprints_s2 * 0.20) + (gs_s2 * 0.60)

media_final = (media_s1 * 0.40) + (media_s2 * 0.60)

def calcular_nota_exame(media_final):
    if media_final >= 6.0:  
        return "Você já está Aprovado! Não precisa fazer exame."
    elif media_final < 2.0:
        return "Média abaixo de 4.0. Reprovado direto (sem direito a exame)."
    else:
        nota_necessaria = 12.0 - media_final
        return f"Você precisa tirar no mínimo {nota_necessaria:.2f} no Exame para ser aprovado."

print('\n==================================')
print(f'Média 1º Semestre: {media_s1:.2f}')
print(f'Média 2º Semestre: {media_s2:.2f}')
print(f'Média Final Anual: {media_final:.2f}')
print('==================================')

if media_final >= 6.0:
    print('Status: APROVADO!')
elif media_final >= 2.0:
    print('Status: EXAME')
    print(calcular_nota_exame(media_final))
else:
    print('Status: REPROVADO')




