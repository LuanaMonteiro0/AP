# listas
print("===CADASTRO DE ALUNOS===")
listaNomes = []
listaNotasProva = []
listaNotasTrabalho = []
listaFrequencia = []
listaMedia = []
espertinhos = []
# virgula = [1:",", 2:"."]
# positivo = {1: "Sim", 2: "sim", 3: "S", 4: "s", 5: "SS", 6: "ss"}
# negativo = {1: "Não", 2: "não", 3: "N", 4: "n", 5: "NN", 6: "nn"}
continuar = "sim"
opcao = -1
media = 0
frequencia = 0
while opcao != 0:
    print(f"MENU")
    print(f"0 - Sair")
    print(f"1 - Cadastrar alunos")
    print(f"2 - Mostrar listas")
    print('3 - calcular a media')
    print('4 - dado o nome de um aluno informar sua média final')
    print('5 - Criar lista com todos os alunos com a nota maior que 8')
    print('6 - status dos alunos')
    opcao = int(input("Qual a opcao desejada? "))
    if opcao == 1:
 #   while continuar in positivo.values():
        aluno = input("Qual o nome do aluno? ")
        listaNomes.append(aluno)
        notasProva = float(input(f"Qual a nota da prova de {aluno}? "))
        listaNotasProva.append(notasProva)
        notasTrabalho = float(input(f"Qual a nota de trabalho de {aluno}? "))
        listaNotasTrabalho.append(notasTrabalho)
        frequencia = int(input(f"Qual a frequencia de {aluno}? "))
        listaFrequencia.append(frequencia)
        media = notasProva*0.7 + notasTrabalho*0.3
        listaMedia.append(media)
       # if media > 8:
           # espertinhos.append(aluno)

     #   continuar = input("Deseja cadastrar um novo aluno? ")
      #  if continuar in negativo.values():
       #     break

        # if continuar not in (negativo.values() and positivo.values()):
          #  while continuar not in (negativo.values() and positivo.values()):
           #     continuar = (input("Valor não compreendido, deseja continuar? "))
            #    if continuar in positivo.values():
             #       continuar = "sim"
              #  elif continuar in negativo.values():
               #     opcao = -1
                #    break
    elif opcao == 2:
        for i in range(len(listaFrequencia)):
            print(f'Aluno #{str(i + 1)}')
            print(f'nome: {listaNomes[i]}')
            print(f'nota prova: {str(listaNotasProva[i])}')
            print(f'nota trabalho: {str(listaNotasTrabalho[i])}')
            print(f'frequencia: {str(listaFrequencia[i])}')
    elif opcao == 3:
        for i in range(len(listaFrequencia)):
            print(f'Aluno #{str(i + 1)}')
            print(f'nome: {listaNomes[i]}')
            print(f'nota prova: {str(listaNotasProva[i])}')
            print(f'nota trabalho: {str(listaNotasTrabalho[i])}')
            print(f'media: {str(listaMedia[i])}')
    elif opcao == 4:
        nomeAluno = input("Digite o nome do aluno: ")
        existe = False
        for i in range(len(listaNomes)):
            if nomeAluno == listaNomes[i]:
                print(f'media: {str(listaMedia[i])}')
                existe = True
        if existe == False:
            print("Aluno não cadastrado!")
    elif opcao == 5:
        espertinhos = []
        for i in range(len(listaMedia)):
            if listaMedia[i] > 8:
                espertinhos.append(listaNomes[i])
        print(espertinhos)
    elif opcao == 6:
        for i in range(len(listaNomes)):
          #  aprovado = (listaMedia[i] >= 6) and (listaFrequencia[i] >= 75)
          #  ifa = (4 >= listaMedia[i] < 6) and (listaFrequencia[i] >= 75)
           # reprovado = (listaMedia[i] < 4) or (listaFrequencia[i] < 75)
            if (listaMedia[i] >= 6) and (listaFrequencia[i] >= 75):
                print(f"{listaNomes[i]} foi aprovado!")
            elif (4 >= listaMedia[i] < 6) and (listaFrequencia[i] >= 75):
                print(f"{listaNomes[i]} ficou de ifa :(")
            elif (listaMedia[i] < 4) or (listaFrequencia[i] < 75):
                print(f"{listaNomes[i]} foi reprovado :)")
