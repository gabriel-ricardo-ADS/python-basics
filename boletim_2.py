
def calculo_cp(semestre):
    cp1_front = float(input(f'Digite sua nota do Checkpoint 1 (Front) {semestre}: '))
    cp2_front = float(input(f'Digite sua nota do Checkpoint 2 (Front) {semestre}: '))
    cp3_front = float(input(f'Digite sua nota do Checkpoint 3 (Front) {semestre}: '))
    cps_front = [cp1_front, cp2_front, cp3_front]
    media_cps_front = (sum(cps_front) - min(cps_front)) / 2 
    cp1_java = float(input(f'Digite sua nota do Checkpoint 1 (Java) {semestre}: '))
    cp2_java = float(input(f'Digite sua nota do Checkpoint 2 (Java) {semestre}: '))
    cp3_java = float(input(f'Digite sua nota do Checkpoint 3 (Java) {semestre}: '))
    cps_java = [cp1_java, cp2_java, cp3_java]
    media_cps_java = (sum(cps_java) - min(cps_java)) / 2 
    cp1_python = float(input(f'Digite sua nota do Checkpoint 1 (Python) {semestre}: ')) 
    cp2_python = float(input(f'Digite sua nota do Checkpoint 2 (Python) {semestre}: '))
    cp3_python = float(input(f'Digite sua nota do Checkpoint 3 (Python) {semestre}: '))
    cps_python = [cp1_python, cp2_python, cp3_python]
    media_cps_python = (sum(cps_python) - min(cps_python)) / 2 
    cp1_eng_soft = float(input(f'Digite sua nota do Checkpoint 1 (Engenharia de Software) {semestre}: '))
    cp2_eng_soft = float(input(f'Digite sua nota do Checkpoint 2 (Engenharia de Software) {semestre}: '))
    cp3_eng_soft = float(input(f'Digite sua nota do Checkpoint 3 (Engenharia de Software) {semestre}: '))
    cps_eng_soft = [cp1_eng_soft, cp2_eng_soft, cp3_eng_soft]
    media_cps_eng_soft = (sum(cps_eng_soft) - min(cps_eng_soft)) / 2 
    cp1_ia = float(input(f'Digite sua nota do Checkpoint 1 (Inteligência Artificial) {semestre}: '))
    cp2_ia = float(input(f'Digite sua nota do Checkpoint 2 (Inteligência Artificial) {semestre}: '))
    cp3_ia = float(input(f'Digite sua nota do Checkpoint 3 (Inteligência Artificial) {semestre}: '))
    cps_ia = [cp1_ia, cp2_ia, cp3_ia]
    media_cps_ia = (sum(cps_ia) - min(cps_ia)) / 2 
    cp1_database = float(input(f'Digite sua nota do Checkpoint 1 (Banco de Dados) {semestre}: '))
    cp2_database = float(input(f'Digite sua nota do Checkpoint 2 (Banco de Dados) {semestre}: '))
    cp3_database = float(input(f'Digite sua nota do Checkpoint 3 (Banco de Dados) {semestre}: '))
    cps_database = [cp1_database, cp2_database, cp3_database]
    media_cps_database = (sum(cps_database) - min(cps_database)) / 2 
    media_total_cp = ((media_cps_front + media_cps_java + media_cps_python + media_cps_eng_soft + media_cps_ia + media_cps_database) / 6) * 0.2
    return media_total_cp

def calculo_challenge(semestre):
    front = float(input(f'Digite sua nota de Front-End (challenge) {semestre}: '))
    java = float(input(f'Digite sua nota de Java (challenge) {semestre}: '))
    python = float(input(f'Digite sua nota de Python (challenge) {semestre}: '))
    eng_soft = float(input(f'Digite sua nota de Engenharia de Software (challenge) {semestre}: '))
    ia = float(input(f'Digite sua nota de Inteligência Artificial (challenge) {semestre}: '))
    database = float(input(f'Digite sua nota de Banco de Dados (challenge) {semestre}: '))
    challenge = [front, java, python, eng_soft, ia, database]
    media_challenge = (sum(challenge) / len(challenge)) * 0.2

    return media_challenge

def calculo_gs(semestre):
    gs_front = float(input(f'Digite sua nota na Global Solution em Front-End {semestre}: '))
    gs_java = float(input(f'Digite sua nota na Global Solution em Java {semestre}: '))
    gs_python = float(input(f'Digite sua nota na Global Solution em Python {semestre}: '))
    gs_eng_soft = float(input(f'Digite sua nota na Global Solution em Engenharia de Software {semestre}: '))
    gs_ia = float(input(f'Digite sua nota na Global Solution em Inteligência Artificial {semestre}: '))
    gs_database = float(input(f'Digite sua nota na Global Solution em Banco de Dados {semestre}: '))
    gs = [gs_front, gs_java, gs_python, gs_eng_soft, gs_ia, gs_database]
    media_gs = (sum(gs) / len(gs)) * 0.6

    return media_gs

print('---BEM VINDO À CALCULADOR DE MÉDIA FINAL---')    

cp_s1 = calculo_cp('1º Semestre')
challenge_s1 = calculo_challenge('1º Semestre')
gs_s1 = calculo_gs('1º Semestre')

media_s1 = cp_s1 + challenge_s1 + gs_s1

cp_s2 = calculo_cp('2º Semestre')
challenge_s2 = calculo_challenge('2º Semestre')
gs_s2 = calculo_gs('2º Semestre')

media_s2 = cp_s2 + challenge_s2 + gs_s2

media_final = ((media_s1 * 0.4) + (media_s2 * 0.6)) / 2

if media_final >= 6:
    print(f'Parabéns! Você foi aprovado com média final de {media_final:.2f}.')
elif media_final >= 2:
    print(f'Você está de EXAME com média final de {media_final:.2f}.')
    nota_exame = float(input('Digite sua nota do exame: '))
    media_exame = (media_final + nota_exame) / 2
    print(f'Sua média após o exame é de {media_exame:.2f}.')
    if media_exame >= 6:
        print(f'Parabéns! Você foi aprovado após o exame com média final de {media_exame:.2f}.')
    else:
        print(f'Infelizmente você foi REPROVADO após o exame com média final de {media_exame:.2f}.')
else:
    print(f'Infelizmente você foi REPROVADO com média final de {media_final:.2f}.')

