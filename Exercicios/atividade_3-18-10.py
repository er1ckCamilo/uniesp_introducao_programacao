'''
Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;

'''
from operator import xor
from random import randint

RAND_MIN = 1
RAND_MAX = 100

# Gerando uma lista de numeros
lista_numeros = []

n = 0
while n < 20:
    numero = randint(RAND_MIN , RAND_MAX)
    lista_numeros.append(numero)
    n += 1

menor = lista_numeros[0]
maior = lista_numeros[0]

for i in lista_numeros:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i

posicao_menor_numero = posicao_maior_numero = posicao = 0
while posicao < len(lista_numeros):
    if lista_numeros[posicao] == maior:
        posicao_maior_numero = posicao
    elif lista_numeros[posicao] == menor:
        posicao_menor_numero = posicao
    posicao += 1

print(f'Lista: {lista_numeros}')
print(f'Menor numero: {menor} e sua posicao: {posicao_menor_numero}\n\
Maior numero: {maior} e sua posicao: {posicao_maior_numero}')




