"""
    Problema 1: As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia. e R$ 1,00 se forem compradas
    pelo menos 12. Escreva um porgrama que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
"""
print('[ ! ] PROMOÇÃO: A partir de 12 maçãs, o valor de cada uma será R$ 1,00. Valor normal R$ 1,30 [ ! ]')
macas = int(input('Digite o número de maçãs que deseja comprar (0 Para sair do programa): '))

preco_promocao = 1.00
preco_normal = 1.30

if macas == 0: # Se digitado 0, encerra o programa
    print('Até mais !')
    exit(0)
elif macas < 0: # Caso digite um número negativo, mostra essa mensagem de "Erro"
    print(f'O número digitado é negativo: {macas}')
    exit(1)
elif macas >= 12: # Calcula o valor total incluso o valor da promoção  
    total = preco_promocao * macas
    print(f'Você comprou {macas} e faz parte da promoção. Valor total: R$ {total}')
else: # Calculando com o valor normal
    total = preco_normal * macas
    print(f'Você comprou {macas} e não faz parte da promoção. Valor total: R$ {total}')