numeros = []
g = -1

while g != 0:
    g = int(input("numero: "))
    if g != 0:
        numeros.append(g)
    if g == 0:
        break

numerossemrep = set(numeros)
print(f"a lista é {numerossemrep}")
somatot = sum(numerossemrep)
qnttot = len(numerossemrep)
medianumeros = somatot/qnttot
print(f"A media dos numeros é {round(medianumeros)}")

for z in numerossemrep:
    if z % 2 == 0:
        posicao = numeros.index(z)
        print(f"O numero {z} é par e está na posição {posicao}")
