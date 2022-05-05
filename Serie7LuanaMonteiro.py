# exercício 7 - Luana Monteiro Ap1s1
n = int(input('Digite o valor de n : '))
numerador = 1
denominador = 1
serie = 'S = '
soma = 0

for i in range(n):
    soma = soma + numerador/denominador

    termo = str(numerador) + '/' + str(denominador)
    numerador = numerador + 1
    denominador = denominador + 2
    if (i+1) != n:
        serie = serie + termo + " + "
    else:
        serie = serie + termo + " = "

print(serie + str(round(soma, 3)))
