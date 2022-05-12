# 1 Matrizes - Hotel Luana Monteiro
hospedagens = []
opcao = -1
quartos = {"c1": "Simples", "c2": "Luxo", "c3": "Presidencial"}
atualizados = 0
print(f"====MENU====\n"
      f"0- Sair do programa\n"
      f"1- Incluir novos hospedes \n"
      f"2- listar todas as hospedagens cadastradas\n"
      f"3- Listar todos os hospedes cadastrados \n"
      f"4- Informações adicionais do hospede pelo nome \n"
      f"5- Atualizar dados de um hospede \n"
      f"6- Exibir os hospedes de um quarto \n"
      f"7- Exibir a quantidade de hospedes que foram atualizados \n"
      f"8- Exibir a media de idade dos hospedes que estão hospedados nos quartos Simples \n"
      f"9- Hospede mais velho \n")

while opcao != 0:
    opcao = int(input(f"Digite a opção desejada: "))

    if opcao == 1:
        hosp = int(input(f"Quantos hospedes deseja incluir? "))
        for i in range(hosp):
            hospede = []
            rep = -1
            nome = ''
            while rep != 0:
                nome = input(f"Qual o nome do {i + 1}º hospede? ")
                existe = False
                for n in range(len(hospedagens)):
                    if hospedagens[n][0] == nome:
                        existe = True
                if existe is False:  # troquei o == pelo is para sumir a coisa amarela dbaixo do codigo
                    hospede.append(nome)
                    rep = 0
                elif existe is True:  # troquei o == pelo is para sumir a coisa amarela dbaixo do codigo
                    print(f"Nome ja cadastrado")
                    rep = 2
            idade = int(input(f"Qual a idade de {nome}? "))
            quarto = quartos["c" + input(f"Qual quarto será o de {nome}?\n"
                                         f"1-Simples ou 2-Luxo ou 3-Presidencial ")]
            hospede.append(idade)
            hospede.append(quarto)
            hospedagens.append(hospede)

    elif opcao == 2:
        if len(hospedagens) != 0:
            print("As hospedagens do dia foram: ")
            for i in range(len(hospedagens)):
                print(hospedagens[i])
        elif len(hospedagens) == 0:
            print(f"Não houveram hospedagens no dia de hoje!")

    elif opcao == 3:
        print(f"Os hospedes cadastrados foram: ")
        for i in range(len(hospedagens)):
            print(hospedagens[i][0])

    elif opcao == 4:
        pessoa = input("Qual hospede deve ser buscado? ")
        entrei = False
        for i in range(len(hospedagens)):
            if pessoa == hospedagens[i][0]:
                print(f"{i+1}º hospede cadastrado\n"
                      f"Nome: {hospedagens[i][0]}\n"
                      f"Idade: {hospedagens[i][1]}\n"
                      f"Quarto: {hospedagens[i][2]}\n")
                entrei = True
        if entrei is False:
            print(f"Não houveram hospedes cadastrados com este nome")

    elif opcao == 5:
        pessoa = input("Qual hospede deve ser atualizado? ")
        entrei = False
        for i in range(len(hospedagens)):
            if pessoa == hospedagens[i][0]:
                atualizados += 1
                sopcao = -1
                entrei = True
                print(f"{i + 1}º hospede cadastrado\n"
                      f"Qual informação deve ser atualizada?\n")
                while sopcao != 0:
                    sopcao = int(input(f"1-Nome ou 2-Idade ou 3-Quarto\n"
                                       f"ou 0-Caso queira cancelar a edição"))
                    if sopcao == 1:
                        velhoNome = hospedagens[i][0]
                        novoNome = input(f"Como devemos chamar {hospedagens[i][0]} apartir de agora?")
                        hospedagens[i][0] = novoNome
                        print(f"O hospede {velhoNome} foi atualizado no sistema para {novoNome}")
                        sopcao = 0
                    elif sopcao == 2:
                        velhaIdade = hospedagens[i][1]
                        novaIdade = int(input(f"Qual a nova idade de {hospedagens[i][0]}?"))
                        hospedagens[i][1] = novaIdade
                        print(f"A idade de {hospedagens[i][0]} foi atualizada de {velhaIdade} para {novaIdade} ")
                        sopcao = 0
                    elif sopcao == 3:
                        velhoQuarto = hospedagens[i][2]
                        novoQuarto = quartos["c" + input(f"Qual quarto será o de {hospedagens[i][0]}?\n"
                                                         f"1-Simples ou 2-Luxo ou 3-Presidencial ")]
                        hospedagens[i][2] = novoQuarto
                        print(f"O quarto de {hospedagens[i][0]} foi  atualizado de {velhoQuarto} para {novoQuarto}")
                        sopcao = 0
                    elif sopcao == 0:
                        print(f"Edição cancelada")
                        atualizados -= 1
                        entrei = False
                        break

        if entrei is False:
            print(f"Não houveram hospedes cadastrados com este nome")

    elif opcao == 6:
        qualQuarto = quartos["c" + input("Qual tipo de quarto da busca? 1 - Simples ou 2 - Luxo ou 3 - Presidencial?")]
        if qualQuarto != "Simples" and qualQuarto != "Luxo" and qualQuarto != "Presidencial":
            print("Valor invalido, tente outro valor! ")
            opcao = 6
        qtd = 0
        liQNomes = []
        e = False
        for i in range(len(hospedagens)):
            if qualQuarto == hospedagens[i][2]:
                qtd += 1
                liQNomes.append(hospedagens[i][0])
                e = True
        print(f"Nos quartos {qualQuarto} os hospedes:\n"
              f"{liQNomes}\n"
              f"estão hospedados")
        if len(hospedagens) == 0:
            print(f"Não houveram hospedagens hoje")
        elif e is False:
            print(f"Não houveram cadastros no quarto {qualQuarto} hoje")

    elif opcao == 7:
        print(f"Hoje foram atualizados {atualizados} hospedes!")
    elif opcao == 8:
        soma = 0
        qtd = 0
        media = 0
        for i in range(len(hospedagens)):
            if "Simples" == hospedagens[i][2]:
                soma += hospedagens[i][2]
                qtd += 1
        if qtd > 0:
            media = soma/qtd
            print(f"A media das idades dos hospedes nos quartos simples é {media}")
        else:
            print("Não houveram hospedagens nos quartos simples hoje!")

    elif opcao == 9:
        maisVelho = -1
        nomeMaisVelho = "ajsd"
        for i in range(len(hospedagens)):
            if maisVelho < hospedagens[i][1]:
                maisVelho = hospedagens[i][1]
                nomeMaisVelho = hospedagens[i][0]
        if maisVelho != -1:
            print(f"O Hospede mais velho é {nomeMaisVelho} com {maisVelho} anos")
            