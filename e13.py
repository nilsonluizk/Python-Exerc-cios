#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo 
# que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Qual a altura: "))

print("[1] Peso ideal para homem.")
print("[2] Peso ideal para mulheres.")
choice = input()

if choice == "1":
 print('Seu peso ideal:{}\n'.format((72.7*altura) - 58))
elif choice == "2":
 print('Seu peso ideal:{}\n'.format((62.1*altura) - 44.7))
else:
 print("Opção incorreta.")