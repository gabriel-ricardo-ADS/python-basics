dict_class = {"Amora": 9.0, "Beatriz": 8.0, "Carla": 7.8, "Daniela": 9.5, "Eduardo": 6.0, "Fernanda": 8.5, "Gabriel": 7.0, "Heloisa": 9.2, "Isabela": 8.8, "João": 6.5}
def media_turma(dicionario):
    soma = 0
    for valor in dicionario.values():
        soma += valor
    media = soma / len(dicionario)
    return media
print(media_turma(dict_class))