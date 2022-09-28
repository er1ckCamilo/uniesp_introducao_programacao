"""
    Problema: Construa um algoritmo para calcular as raizes de uma equação do 2 grau (Ax² + Bx + C),
    sendo que os valores A,B,C são fornecidos pelo usuário. (Considere que a equação possui duas raizes reais)
"""

def f_delta(a,b,c): # Função para calcular o valor de delta
    delta = b ** 2 - 4 * a * c 
    return delta

def f_x(a,b,c): # Calcula o valor das raizes e retorna em uma tupla.
    
    delta = f_delta(a,b,c) # Encontrando o delta
    raiz_delta = f_raiz(delta) # Obtendo a raiz do delta
    
    x = (-b + raiz_delta) / (2*a)
    x2 = (-b - raiz_delta) / (2*a)

    return (x,x2) # Retorna o resultado

def f_raiz(radicando): # Encontrando a raiz de um número (Essa forma de encontrar a raiz não é nada eficiente. apenas para exemplos)
    raiz = 0
    for numero in range(1,radicando + 1):
        if not numero % 2 == 0: # Se o resto da divisão do numero por 2 não for igual 0, o numero é impar, então calcule o radicando
           radicando = radicando - numero
           raiz += 1
           if radicando == 0: # Se o radicando for igual 0, retorne uma raiz exata
                return raiz

A = int(input('Digite um valor para A: '))
B = int(input('Digite um valor para B: '))
C = int(input('Digite um valor para C: '))

resultado = f_x(A,B,C)
print(f'Resultado: x = {resultado[0]} / x2 = {resultado[1]}')