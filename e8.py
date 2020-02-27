import locale

locale.setlocale( locale.LC_ALL, 'pt_BR' )

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
def main():
    print("*** Cálculo de horas trabalhadas ***")
    slario = float(input("Digite quanto você ganha por hora: "))
    hrs = int(input("Digite quantidade de horas trabalhadas no mês: "))

    currency = locale.currency((slario * hrs), grouping=True)

    print("Você receberá no mês o valor de: R$ {}".format(currency))

main()  