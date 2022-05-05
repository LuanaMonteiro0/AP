# listas - ex 1 - Luana Monteiro ap1s1
print("===NUMEROS===")
from random import randint
lista = []
pares = 0
impares = 0
while len(lista) < 5:
    numero = randint(1, 10)
    if numero not in lista:  # usado pra não repetir numeros
        lista.append(numero)
    if numero == 1:
        impares += 1
    elif numero == 10:
        pares += 1
    elif numero % 2 == 0 and (numero != 10 and numero != 1):  # precisei por essa condição pois os
        pares += 1                                            # numeros que eram gerados consideravam
    elif numero % 2 == 1 and (numero != 10 and numero != 1):  # 10 impar e 1 par - n sei pq
        impares += 1
    if len(lista) == 5:
        break
maior = max(lista)
menor = min(lista)
print(f"A lista gerada foi {lista}")
print(f"O maior numero da lista é {maior}")
print(f"O menor numero da lista é {menor}")
if pares > impares:
    print(f"Existem mais numeros pares, eles são {pares}")
    print(f"Exitem {impares} numeros impares")
else:
    print(f"Existem mais numeros impares, eles são {impares}")
    print(f"Exitem {pares} numeros pares")
