#Faça um Programa que peça dois números e imprima a soma.
def main():
    print("*"*50)
    soma1 = int(input("Digite um número para a primeira adição: "))
    soma2 = int(input("Digite um número para a segunda adição: "))
    print("*"*50)

    print("O resultado da soma de {} + {} é igual a {}".format( soma1, soma2, (soma1 + soma2) ))
    
main()