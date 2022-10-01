# Created by: Erick, P1A Sis. Internet

from os import system
from math import sqrt
from sys import stderr

class Equacao2grau:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def f_delta(self): # Função para calcular o valor de delta
        delta = self.b ** 2 - 4 * self.a * self.c 
        return delta

    def f_x(self): # Calcula o valor das raizes e retorna em uma tupla.
    
        delta = self.f_delta() # Encontrando o delta
        raiz_delta = self.f_raiz(delta) # Obtendo a raiz do delta
    
        if delta <= 0: # Retorna None caso não seja possivel considerar 2 raizes
            return None

        x = (-self.b + raiz_delta) / (2*self.a)
        x2 = (-self.b - raiz_delta) / (2*self.a)

        return (x,x2) # Retorna o resultado

    def f_raiz(self,radicando): # Encontrando a raiz de um número (Essa forma de encontrar a raiz não é nada eficiente. apenas para exemplos)
        raiz = 0
        for numero in range(1,int(radicando) + 1):
            if not numero % 2 == 0: # Se o resto da divisão do numero por 2 não for igual 0, o numero é impar, então calcule o radicando
                radicando = radicando - numero
                raiz += 1
                if radicando == 0: # Se o radicando for igual 0, retorne uma raiz exata
                    return raiz 
                elif radicando - numero < 0: # Se a raiz não for exata, os valores vão ser aproximados. :)
                    return raiz + 1

class Calculadora:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def somar(self):
        return self.n1 + self.n2
    
    def subtrair(self):
        return self.n1 - self.n2
    
    def multiplicar(self):
        return self.n1 * self.n2
    
    def dividir(self):
        return self.n1 / self.n2
    
    def potencia(self):
        return self.n1 ** self.n2


system('cls')
print('\t\t<======> Escolha uma opção ( 0 Para sair ) <======>\n')
print('\t(1) FORBELLONE.1\t(2) FORBELLONE.2\t(3) Calculadora')
print('\t(4) IMC\t(5) Intervalos entre números\t(6) Sequência de valores')
escolha = int(input('> '))

if escolha == 0:

    print('Até mais')
    exit(0)

elif escolha == 1: # Problema 1

    system('cls')
    A = int(input('Digite um valor para A: '))
    B = int(input('Digite um valor para B: '))
    C = int(input('Digite um valor para C: '))

    equacao = Equacao2grau(A,B,C)
    resultado = equacao.f_x()

    if resultado == None:
        print('[ ! ] O programa considera apenas duas raizes. Digite outro valor para A e C [ ! ]')
    else:
        print(f'Resultado: x = {resultado[0]} / x2 = {resultado[1]}')

elif escolha == 2: # Problema 2

    system('cls')
    x1 = float(input('Digite o valor de x1: '))
    x2 = float(input('Digite o valor de x2: '))
    y1 = float(input('Digite o valor de y1: '))
    y2 = float(input('Digite o valor de y2: '))

    d = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
    resultado = sqrt(d)
    print(f'Distância entre os pontos: {resultado}')

elif escolha == 3: # Problema 3

    system('cls')
    print('\t\t<======> Escolha uma operação ( ! Para sair ) <======>\n')
    print('\t(+) Adição (-) Subtração (*) Multiplicação (/) Divisão (**) Potenciação')
    op = input('>')

    system('cls')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    calc = Calculadora(n1,n2)

    if op == '!':
        exit(0)
    elif op == '+':
        calc.somar()
    elif op == '-':
        calc.subtrair()
    elif op == '*':
        calc.multiplicar()
    elif op == '/':
        calc.dividir()
    elif op == '**':
        calc.potencia()
    else:
        print('[ ! ] Opção desconhecida', file=stderr)
        exit(1)

elif escolha == 4: # Problema 4 

    system('cls')
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    imc = peso / altura ** 2

    if imc < 18.5:
        print(f'IMC: {imc} | Classificação: Abaixo do peso')
    elif imc >= 18.5 and imc <= 25:
        print(f'IMC: {imc} | Classificação: Peso normal')
    elif imc >= 25 and imc <=30:
        print(f'IMC: {imc} | Classificação: Acima do peso')
    elif imc > 30:
        print(f'IMC: {imc} | Classificação: Obeso')
    else:
        print('[ ! ] Atenção: Algo de errado não está certo [ ! ] ')

elif escolha == 5: # Problema 5
    
    system('cls')
    print('\t\t<======> Digite números. Digite um número negativo para sair <======>\n')

    a = b = c = d = f = num = 0
    while num >= 0:
        num = int(input('> '))

        if num >= 0 and num <= 25:
            a += 1
        elif num >= 26 and num <= 50:
            b += 1
        elif num >= 51 and num <= 75:
            c += 1
        elif num >= 76 and num <= 100:
            d += 1
        else:
            f += 1
    
    print(f'Intervalo entre 0 e 25: {a}')
    print(f'Intervalo entre 26 e 50: {b}')
    print(f'Intervalo entre 51 e 75: {c}')
    print(f'Intervalo entre 76 e 100: {d}')
    print(f'Fora dos intervalos: {f}')

elif escolha == 6: # Problema 6
    
    system('cls')
    x = int(input('Digite um número: '))

    resultado = 1
    for num in range(1, x + 1):
        resultado = num * resultado
    
    print(f'{x}! =',end=' ')
    while x > 1:
        print(f'{x} X',end=' ')
        x -= 1
    print(f'1 = {resultado}')

else:
    print('[ ! ] Opção desconhecida', file=stderr)
    exit(1)