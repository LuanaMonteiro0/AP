# Exercício 9 - Luana Monteiro

from random import randint
nGerados = []
nPares = []
numeros = - 1
while numeros != 50:
    numeros = randint(0, 100)
    nGerados.append(numeros)
    if numeros == 50:
        for E in nGerados:
            avaPar = E % 2
            if avaPar == 0:
                nPares.append(E)
print("Foram gerados " + str(len(nPares)) + " numeros pares")
print(str(nGerados))
print(str(nPares))
