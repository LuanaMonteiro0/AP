prodA = 10000
crescA = 1.15

prodB = 8000
crescB = 1.20

ano = 1
while prodA > prodB:
    print('Ano ' + str(ano))
    prodA = prodA * crescA
    print('Nova produção A: ' + str(round(prodA, 2)))

    prodB = prodB * crescB
    print('Nova produção B: ' + str(round(prodB, 2)))
    ano  = ano + 1

print('Qtdd de anos necessarios : ' + str(ano-1))
