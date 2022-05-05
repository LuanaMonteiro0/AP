from random import randint
qntdtot = 0
qntdpares = 0
somadsete = 0
qntddsete = 0
qntddivsete = 0
i = -1
while i % 34 != 0:
    i = randint(89, 297)
    print(i)
    qntdtot += 1
    if i % 17 == 0:
        qntddsete += 1
        somadsete += i
        # print("entrou cond 1\n")
    if (100 <= i <= 200) and (i % 2 == 0):
        qntdpares += 1
        # print("entrou cond 2\n")
    if (i % 7 == 0) and (i >= 183):
        qntddivsete += 1
        # print("Entrou cond 3\n")
    if i % 34 == 0:
        # print("Parada\n\n")
        break

mediadsete = somadsete / qntddsete
porcpares = qntdpares / qntdtot * 100
print(f"A qntd de numeros gerados foi {qntdtot}")
print(f"A) a media dos valores divisiveis por 17 é {round(mediadsete)}")
print(f"B) a porcentagem de pares gerados entre 100 e 200 é {round(porcpares, 2)}%")
print(f"C) a qntd de divisiveis por sete maiores que 183 é {qntddivsete}")
