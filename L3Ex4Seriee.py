# 4. Leia o valor de elementos da série, imprima a mesma e calcule o valor:
# S = 2/4 - 3/9 + 4/16 – 5/25 + 6/36 - .... + n/m
serie = "S = "
cnt = 0
rFinal = 0
n = int(input("Qual o valor deve ser gerado na serie? "))
forElem = n + 1
serieFinal = ""
for i in range(2, forElem):
    n = i
    m = n ** 2
    cnt += 1
    ele = n/m
    escrito = str(n) + "/" + str(m)
    serie = serie + escrito
    if (cnt % 2 != 0) and ((i + 1) != n):
        serie += " - "
        rFinal -= ele
    elif (cnt % 2 != 1) and ((i + 1) != n):
        serie += " + "
        rFinal += ele
    serieFinal = serie[:-3]
    serieFinal += " = "
rFinal = rFinal * (-1)
print(serieFinal + str(round(rFinal, 5)))
