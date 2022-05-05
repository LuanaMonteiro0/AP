# exercício 2 - Luana Ap1s1

op = 4
while op != 0:
    tabu = float(input("Digite o numero desejado para a tabuada: "))
    print("\n TABUADA DO " + str(tabu) + "\n")
    for i in range(0, 11):
        result = tabu * i
        print(str(i) + ' x ' + str(tabu) + ' = ' + str(result))
    op = int(input("Deseja visualizar outra tabuada? 1 - sim ou 0 - não "))
