# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tam = int(input("Digite o tamanho do arquivo para download (em MB): "))
vel = int(input("Digite a velocidade da sua internet (em Mbps): "))
conversao = tam/(vel/8)
print("Tempo para download em MINUTOS: {}".format(conversao/60))
print("Tempo para download em SEGUNDOS: {}".format(conversao))
