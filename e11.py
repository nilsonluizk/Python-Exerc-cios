# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro  metade do segundo.
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.com
inteiro1 = int(input("Digite um número inteiro: "))
inteiro2 = int(input("Digite um número inteiro: "))
real = float(input("Digite um número real: "))
print('O produto do dobro do primeiro com metade do segundo:{}'.format((2*inteiro1) + (inteiro2/2)))
print('A soma do triplo do primeiro com o terceiro: {}'.format((3 * inteiro1) + real))
print('O terceiro elevado ao cubo: {}'.format(pow(real, 3)))
