# Ted 10/11 Erick Gonçalves P1B

from random import randint
from sys import stderr

def At_clubes():

    print('*** Digite 10 Clubes ***')
    clubes = []

    for i in range(1,11):
        clube = input(f'Digite o {i} clube: ')
        clubes.append(clube)

    clube_escolhido = input('Escolha um clube: ')
    if clube_escolhido in clubes:
        print('Achei !!')
    else:
        print('Não achei')

def At_numeros():

    print('*** Gerando Numeros ***')
    numeros = []
    count = 0

    while count < 30:
        n = randint(0, 100)
        numeros.append(n)
        count += 1
    
    numero = int(input('Escolha um numero: '))
    count = 0
    for i in numeros:
        if i == numero:
            count += 1
    print(numeros)
    print(f'O numero escolhido {numero} apareceu {count} vezes')

while True:
    print('Escolha uma opção: (0) Sair (1) Escolher times (2) Escolher um numero')
    op = int(input('> '))

    if op < 0 or op > 2:
        print(f'Opção {op} invalida', file=stderr)
        exit(1)
    elif op == 0:
        print('Até mais !')
        break
    elif op == 1:
        At_clubes()
    elif op == 2:
        At_numeros()