# exercício 6 fatoriais - Luana Monteiro Ap1s1
print("===FATORIAIS===")
op = 1
while op != 2:
    inputNum = float(input("Qual numero deseja calcular a fatorial? "))
    contar = 1
    fim = 1

    while inputNum >= contar:
        fim = fim * contar
        contar = contar + 1

    print("Fatorial de " + str(inputNum) + " é " + str(fim))
    op = int(input("Deseja Calcular outra fatorial? 1-sim ou 2-não "))
