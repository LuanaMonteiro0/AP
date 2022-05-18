opc = -4
cadAlunos = []
cadCarros = []
cadAulas = []
print(f"=====AUTO ESCOLA=====\n"
      f"====MENU====\n"
      f"0- Sair do programa\n"
      f"1- Incluir novos alunos\n"
      f"2- listar alunos por faixa etaria\n"
      f"3- Cadastrar veiculos \n"
      f"4- Listar veículos\n"
      f"5- Registrar uma aula \n"
      f"6- Listar todas as aulas cadastradas \n"
      f"7- Valor arrecadado com idosos\n"
      f"8- Aula para a pessoa mais jovem \n"
      f"9- Inserir pagamento das aulas\n")

while opc != 0:
    opc = int(input(f"Qual opção acessar? "))
    if opc == 1:
        aluno = []
        nome = input(f"Qual o nome do aluno? ")
        existe = False
        for i in range(len(cadAlunos)):
            if nome == cadAlunos[i][0]:
                existe = True
        if existe is True:
            print(f"Nome ja cadastrado, insira outro nome")
            opc = 1
        elif existe is False:
            idade = int(input(f"Qual a idade de {nome}? "))
            sexo = input(f"Qual o sexo de {nome}? Masculino (M) ou Feminino (F)")
            aluno.append(nome)
            aluno.append(idade)
            aluno.append(sexo)
            cadAlunos.append(aluno)
    elif opc == 2:
        xoven = []
        adult = []
        veio = []
        liOrdenada = []
        for i in range(len(cadAlunos)):
            if (cadAlunos[i][1] >= 18) and (cadAlunos[i][1] <= 24):
                xoven.append(cadAlunos[i][0])
            elif (cadAlunos[i][1] >= 25) and (cadAlunos[i][1] <= 64):
                adult.append(cadAlunos[i][0])
            elif cadAlunos[i][1] >= 65:
                veio.append(cadAlunos[i][0])
        liOrdenada.append(xoven)
        liOrdenada.append(adult)
        liOrdenada.append(veio)
        print(f"Alunos jovens: {xoven}\n"
              f"Alunos adultos: {adult}\n"
              f"Alunos idosos: {veio}\n")
    elif opc == 3:
        veiculo = []
        nomeC = input(f"Qual o nome do veículo? ")
        aulas = int(input(f"Qual a quantidade de aulas nesse veiculo? "))
        veiculo.append(nomeC)
        veiculo.append(aulas)
        cadCarros.append(veiculo)
    elif opc == 4:
        print(f"Os veículos e aulas disponiveis são:")
        for i in range(len(cadCarros)):
            print(i)
    elif opc == 5:
        regAula = []
        nAluno = input(f"Qual o nome do aluno dessa aula? ")
        existe = False
        for i in range(len(cadAlunos)):
            if nAluno == cadAlunos[i][0]:
                existe = True
        if existe is False:
            esc = int(input(f"O aluno não foi cadastrado. Deseja cadastrar o aluno? 1-Sim ou 2-Não"))
            if esc == 1:
                opc = 1
            else:
                opc = -4
        else:
            nCarro = input(f"Qual o carros usado nas aulas de {nAluno}? ")
            carroExiste = False
            for i in range(len(cadCarros)):
                if nCarro == cadCarros[i][0]:
                    carroExiste = True
            if existe is False:
                esc = int(input(f"O carro não foi cadastrado. Deseja cadastrar o carro? 1-Sim ou 2-Não"))
                if esc == 1:
                    opc = 3
                else:
                    opc = -4
            else:
                data = input(f"Insira a data da aula de {nAluno}")
                exis = False
                for i in range(len(cadAulas)):
                    if nAluno == cadAulas[i][0]:
                        #  regAula.append(nAluno)
                        #  regAula.append(nCarro)
                        regAula.append(data)
                        cadAulas[i][3] += 30
                        exis = True
                if exis is False:
                    regAula.append(nAluno)
                    regAula.append(nCarro)
                    regAula.append(data)
                    regAula.append(30)
                    cadAulas.append(regAula)

    #  elif opc == 6:
