# Exercício 1 - Luana AP1S1

nmrInput = []
nmrPar = []
rep1 = 3
while rep1 != 0:
    nmr = int(input("Digite um numero inteiro: "))
    nmrInput.append(nmr)
    rep1 = int(input("Digitar outro numero? 0 = não ou 1 = sim "))
for i in nmrInput:
    seraPar = i % 2  # separou os pares
    if seraPar == 0:
        nmrPar.append(i)
qntsNmrs = len(nmrPar)
soma = sum(nmrPar)
media = soma / qntsNmrs
print("A media das soma dos itens pares será: " + str(round(media)))

# correção
# contPares = 0 conta qnts numeros pares foram colocados
# numero = -1 oq o usuario digitar
# soma = 0
# while numero != 0
#   numero = int(input("Digite um numero: ")
#   if numero % 2 == 0: avalia se é par
#       soma = soma + numero ideia de acumulador
#       contPares = contPares + 1
# print("Calculo: ")
# media = soma/contPares
# print("A media é: " + str(media))
#