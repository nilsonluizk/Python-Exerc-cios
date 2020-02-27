import math
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, 
# isto é, considere latas cheias.
m = int(input("Digite quantos metros quadrados serão pintados: "))
metros = (m*0.10) + m
latas = m / 108 # 108 é a quantidade máxima de metros com 18 litros de tinta
galao = m / 21.6 # 21.6  é a quantidade máxima de metros com 3.6 litros de tinta
misturado = metros / 129.6 # 129.6  é a quantidade máxima de metros com 3.6 litros de tinta
print("metros com folga: {}".format((metros)))
print("Latas de tinta de 18 litros: {}".format(math.ceil(latas)))
print("Galões de tinta de 3.6 litros: {}".format(math.ceil(galao)))
print("Valor com galão de R$ 25,00: {}".format(math.ceil(galao)*25))
print("Valor com galão de R$ 80,00: {}".format(math.ceil(latas)*80))
print("Preço com galões de R$ 80 e R$ 25,00: {}".format(math.ceil(misturado)*105))