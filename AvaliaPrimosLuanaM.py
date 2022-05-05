# Escreva um programa que determine se um dado número N (digitado pelo usuário) é
# primo ou não
print('===PRIMOS===')
print('VALORES QUE CONTÉM MAIS DE 20 MULTIPLOS APENAS TERÃO SEUS 20 PRIMEIROS MULTIPLOS DEMONSTRADOS')
repete = 5
while repete != 2:
    N = int(input('Qual valor deve ser avaliado? '))
    qntsMultiplos = 0
    quaisMultiplos = []
    for divisor in range(2, N):
        resultado = N % divisor
        if resultado == 0:
            qntsMultiplos += 1
            quaisMultiplos.append(divisor)
            calmaMultiplos = len(quaisMultiplos)
            if calmaMultiplos >= 20:
                break

    if qntsMultiplos == 0:
        print("Esse é um numero primo")
    elif qntsMultiplos >= 20:
        print("Esse numero não é primo, ele tem mais que " + str(qntsMultiplos) + " multiplos")
        print("sendo os 20 primeiros:")
        print(*quaisMultiplos, sep=" - ")
    else:
        print("Esse numero não é primo, ele tem " + str(qntsMultiplos) + " multiplos")
        print("sendo eles:")
        print(*quaisMultiplos, sep=" - ")
    repete = int(input("Reiniciar programa 1 = sim ou 2 = não "))
