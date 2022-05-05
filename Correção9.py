# exercício 9  - Luana Monteiro ap1s1

from random import randint
contPares = 0
nro = -1
while nro != 50:
    nro = randint(0, 100)
    print(nro)
    if nro % 2 == 0:  # nrm par
        contPares = contPares + 1
print("Foram gerados " + str(contPares) + " numeros pares")
