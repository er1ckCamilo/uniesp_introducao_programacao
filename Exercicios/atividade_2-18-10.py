'''
    Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos. Calcular a média da 
    turma e contar quantos alunos obtiveram nota acima desta média calculada. Escrever a média da turma 
    e o resultado da contagem
'''

# Lista de notas
notas = []

# Armazenando notas na lista
for nota in range(10):
    notas.append(float(input('Digite uma nota: ')))

# Quantidades de notas
quantidade_lista = len(notas)

# Somando todos os elementos da lista
soma = 0
for nota in notas:
    soma = soma + nota

# Obtendo a media
media = soma / quantidade_lista

# Calculando a quantidade de alunos acima da media
quantidade_alunos_media = 0
for nota_aluno in notas:
    if nota_aluno > media:
        quantidade_alunos_media += 1

print(f'Media da turma: {media}\nQuantidade de alunos acima da media: {quantidade_alunos_media}')

