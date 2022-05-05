print('===PRIMOS===')
repete = 5
while repete != 2:
    N = int(input('Qual valor deve ser avaliado? '))
    qntsMultiplos = 0
    for divisor in range(2, N):
        resultado = N % divisor
        if resultado == 0:
            qntsMultiplos += 1

    if qntsMultiplos == 0:
        print("Esse é um numero primo")
    else:
        print("Esse numero não é primo")

    repete = int(input("Reiniciar programa 1 = sim ou 2 = não "))
