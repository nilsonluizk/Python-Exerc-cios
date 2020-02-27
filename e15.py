# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo
import locale

locale.setlocale( locale.LC_ALL, 'pt_BR' )

slario = float(input("Digite quanto você ganha por hora: "))
hrs = int(input("Digite quantidade de horas trabalhadas no mês: "))

salario_bruto = slario * hrs

impostoderenda = salario_bruto * 0.11
inss = salario_bruto * 0.08 
sindicato = salario_bruto * 0.05 
liquido = salario_bruto - (impostoderenda + inss + sindicato)

salario_bruto = locale.currency(salario_bruto, grouping=True)
impostoderenda = locale.currency((impostoderenda), grouping=True)
inss = locale.currency((inss), grouping=True)
sindicato = locale.currency((sindicato), grouping=True)
liquido = locale.currency((liquido), grouping=True)

print("Salário bruto: {}".format(salario_bruto))
print("Valor do Imposto de Renda: {}".format(impostoderenda))
print("Valor do INSS: {}".format(inss))
print("Valor do Sindicato: {}".format(sindicato))
print("Valor do Salário Líquido: {}".format(liquido))