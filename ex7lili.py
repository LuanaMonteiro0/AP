# exercício 7 - lista 4 - Luana  Monteiro
lista1 = []
lista2 = []
listaUniao = []
listaInter =[]
opcao = -1
print(f"===MENU===\n"
      f"0 - sair\n"
      f"1 - Carregar dados da lista 1\n"
      f"2 - Carregar primeiro dado da lista 2 e gerar o restante\n"
      f"3 - Exibir listas\n"
      f"4 - Lista união\n"
      f"5 - Lista Intersecção \n"
      f"6 - Somar o maior valor de todas as listas na lista 1\n"
      f"7 - Multiplicar os elementos das listas\n"
      f"8 - Zerar tudo")
while opcao != 0:
    opcao = int(input(f"Digite a opção desejada: "))
    if opcao == 1:
        if len(lista1) < 5:
            print(f"Lista 1")
            numero = int(input(f"Digite o numero desejado: "))
            lista1.append(numero)
        else:
            print(f"Ja existem 5 elementos cadastrados")
    elif opcao == 2:
        print(f"Lista 2")
        numero = int(input(f"Digite o primeiro numero da lista 2"))
        lista2.append(numero)
        for i in range(4):
            novoNumero = lista2[i] * 2
            lista2.append(novoNumero)
    elif opcao == 3:
        print(f"Listas formadas")
        print(f"A lista 1 é formada por {lista1}")
        print(f"A lista 2 é formada por {lista2}")
        print(f"A lista união é formada por {listaUniao}")
    elif opcao == 4:
        print("Lista união")
        for i in range(len(lista1)):
            existe = False
            for j in range(len(listaUniao)):
                if listaUniao[j] == lista1[i]:
                    existe = True

            if existe == False:
                listaUniao.append(lista1[i])

        for i in range(len(lista2)):
            existe = False
            for j in range(len(listaUniao)):
                if listaUniao[j] == lista2[i]:
                    existe = True

            if existe == False:
                listaUniao.append(lista2[i])

        print(listaUniao)
    elif opcao == 5:
        print(f"Lista intersecção")
        for i in range(len(lista1)):
            for j in range(len(lista2)):
                if lista1[i] == lista2[j]:
                    existe = False
                    for k in range(len(listaInter)):
                        if lista1[i] == listaInter [k]:
                            existe = True
                    if existe == False:
                        listaInter.append(lista1[i])
        print(listaInter)

    elif opcao == 6:
        print(f"Maior Valor")
        maiorr = -1
        for i in range(len(lista1)):
            if lista1[i] > maiorr:
                maiorr = lista1[i]
        for d in range(len(lista2)):
            if lista2[d] > maiorr:
                maiorr = lista2[d]
        print(f"O maior valor é {maiorr}\n"
              f"o valor foi incrementado e na lista 1")
        for x in range(len(lista1)):
            lista1[x] += maiorr

    elif opcao == 7:
        lista3 = []
        if len(lista1) == len(lista2):
            for i in range(len(lista2)):
                lista3.append(lista1[i] * lista2[i])
        else:
            print('Nao é possível fazer a multiplicacao')
        print(lista3)

    elif opcao == 8:
        lista1 = []
        lista2 = []
        listaUniao = []
        listaInter = []
