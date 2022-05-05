from random import randint
nmr = -1
soma = 0
qtdImpar = 0
menor = 51
while nmr != 32:
    nmr = randint(0, 50)
    print(nmr)
    soma = soma + nmr
    if nmr % 2 != 0:
        qtdImpar = qtdImpar + 1
    if nmr < menor:
        menor = nmr
print("Soma dos numeros: " + str(soma))
print("Quantidade de impares: " + str(qtdImpar))
print("O menor numero é: " + str(menor))
