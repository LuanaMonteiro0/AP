# listas - ex 2 - Luana Monteiro ap1s1
print("===NUMEROS===")
from random import randint
lista = []
while len(lista) < 30:
    numero = randint(1, 100)
    if numero not in lista:  # usado pra não repetir numeros
        lista.append(numero)
    if len(lista) == 30:
        break
# print(len(lista) == len(set(lista)))  # usado pra saber se repetiu algum numero (true = não repetiu)
print(f"A lista gerada foi {lista}")

