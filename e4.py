#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def main():
    print("***** Notas bimestrais *****")
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    nota4 = int(input("Digite a quarta nota: "))
    
    print ("A media das notas no bimetre é: {}".format((nota1 + nota2 + nota3 + nota4)/4))

main()