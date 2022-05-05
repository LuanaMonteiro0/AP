# Luana Monteiro - exercício da nota 
alunosL = []
notasL = []
presenca = []
apRep = []

print("==>>AVALIADOR DE APROVAÇÃO<<==")
print("=====CALCULADORA DE NOTAS=====")
nomeProf = input("Professor(a), qual o seu nome? ")
perguntarPresenca = True
opic = "6"
zopic = "9"
while opic != "2":
    print("===DADOS===")
    nomeAluno = input("Qual o nome do(a) aluno(a) cuja nota será calculada? ")
    alunosL.append(nomeAluno)
    notaP1 = float(input("Nota da prova de " + nomeAluno + ": "))
    notaProj = float(input("Nota do trabalho de " + nomeAluno + ": "))
    medilinda = 0
    mediaFInd = 0.7*notaP1 + 0.3*notaProj
    print("prof, " + nomeProf + ", a média do aluno " + nomeAluno + " nesse semestre foi " + str(mediaFInd))
    notasL.append(mediaFInd)
    if mediaFInd >= 6:
        print(nomeAluno + " é elegivel para aprovação")
    elif (mediaFInd >= 4) and (mediaFInd < 6):
        print(nomeAluno + " é elegivel para recuperação")
    else:
        print(nomeAluno + " foi reprovado por nota")
        apRep.append("REPROVADO")
        perguntarPresenca = False
        opic = input("Deseja calcular a aprovação de outro aluno? 1 - sim ou 2 - não: ")
        zopic = opic
    if perguntarPresenca == True:
        print(nomeProf + ", para definir a aprovação ou não do aluno é preciso verificar a % de presença do mesmo")
        print("um aluno cuja presença seja maior ou igual a 75% do período de aulas é elegivel para aprovação")
        aulasRedef = "2"
        print("por padrão existem 26 semanas de aula com 6 aulas por semana totalizando uma qtd N de 156 aulas")
        aulasEsc = input(nomeProf + ", você deseja alterar a quantidade N de aulas? 1 - sim ou 2 - não ")
        essePassa = 75
        seraquepassa = 0
        if aulasEsc == aulasRedef:
            print("Seguindo padrão de quantidade de aulas")
            aulasPre1 = (int(input("Qual o numero de aulas em que o aluno esteve presente? "))*100)/156
            seraquepassa = aulasPre1
            if aulasPre1 >= essePassa:
                print("A presença nas aulas de " + nomeAluno + " é suficiente para ser elegivel para aprovação")
                presenca.append(str(aulasPre1) + "%")
                print("A porcentagem de presença do aluno nesse semestre foi: " + str(aulasPre1))
                opic = input("Deseja calcular a aprovação de outro aluno? 1 - sim ou 2 - não")
            else:
                print("A presença de " + nomeAluno + " é insuficiente, " + nomeAluno + " foi reprovado")
                presenca.append(str(aulasPre1) + "%")
                apRep.append("REPROVADO")
                opic = input("Deseja calcular a aprovação de outro aluno? 1 - sim ou 2 - não: ")
                zopic = opic
        if aulasEsc != aulasRedef:
            qtdNova = (int(input("Insira a quantidade nova de aulas a serem avaliadas: ")))
            aulasPre2 = (int(input("Qual o numero de aulas em que o aluno esteve presente?"))*100)/qtdNova
            seraquepassa = aulasPre2
            if aulasPre2 >= essePassa:
                print("A presença nas aulas de " + nomeAluno + " é suficiente para ser elegivel para aprovação")
                presenca.append(str(aulasPre2) + "%")
                print("A porcentagem de presença do aluno nesse semestre foi: " + str(aulasPre2))
                zopic = opic
            else:
                print("A presença de " + nomeAluno + " é insuficiente, " + nomeAluno + " foi reprovado")
                presenca.append(str(aulasPre2) + "%")
                apRep.append("REPROVADO")
                opic = input("Deseja calcular a aprovação de outro aluno? 1 - sim ou 2 - não: ")
                zopic = opic
        if (seraquepassa >= 75) and (medilinda >= 6):
            print(nomeProf + ", O aluno " + nomeAluno + " foi aprovado.")
            apRep.append("APROVADO")
            opic = input("Deseja calcular a aprovação de outro aluno? 1 - sim ou 2 - não: ")
            zopic = opic

        if (seraquepassa >= 75) and (medilinda >= 4) and (medilinda < 6):
            print(nomeProf + ", O aluno " + nomeAluno + " deve ser encaminhado para recuperação.")
            apRep.append("RECUPERAÇÃO")
            opic = input("Deseja calcular a aprovação de outro aluno? 1 - sim ou 2 - não: ")
            zopic = opic
    perguntarPresenca = True
    if opic == "2":
        # qtddAlunos = 0
        # for aluno in alunosL:
        #    print(aluno + ' - nota : ' + notasL[qtddAlunos] + ' presenca -> ' + presenca[qtddAlunos])
        #    qtddAlunos = qtddAlunos +1
        # não funcionou direito o que sera que aconteceu
        aluNotCon = [item for sublist in zip(alunosL, notasL, presenca, apRep) for item in sublist]
        print("===>RELATÓRIO FINAL<===")
        print("Professor, " + nomeProf + " os resultados dos aprovados e reprovados de hoje foram: ")
        print(aluNotCon)

