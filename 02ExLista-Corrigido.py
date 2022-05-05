from random import randint
lista = []
qtdElem = 0
while qtdElem < 30:
    nro = randint(1, 40)
    existe = False
    for j in range(len(lista)):
        if lista[j] == nro:
            existe = True
            break
    if existe == False:
        lista.append(nro)
        qtdElem += 1
print(lista)