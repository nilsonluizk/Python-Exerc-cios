# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9)
####
#
# Celsius = input()
# Faren = (Celsius*9/5)+32
#
####
#
# Faren = input()
# Celsius = ((Faren-32)*5/9)
#
####
f = float(input("Digite o grau em F: "))
print("O valor em Celsius é: {}".format((f-32)*5/9))
