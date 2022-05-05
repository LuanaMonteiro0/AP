# Tarefa 1 - Ads modulo 1 - programa de calculo de nota
# tentativa de adicionar lista
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
    while zopic != "2":
        print("===DADOS===")
        nomeAluno = input("Qual o nome do(a) aluno(a) cuja nota será calculada? ")
        alunosL.append(nomeAluno)
        notaP1 = float(input("Nota da primeira prova de " + nomeAluno + ": "))
        notaP2 = float(input("Nota da segunda prova de " + nomeAluno + ": "))
        mediaProvas = (notaP1 + notaP2)/2
        print("a media das notas desse aluno foi: " + str(mediaProvas))
        notaExer1 = float(input("Nota do primeiro exercício periodico de " + nomeAluno + ": "))
        notaExer2 = float(input("Nota do segundo exercício periodico de " + nomeAluno + ": "))
        notaExer3 = float(input("Nota do terceiro exercício periodico de " + nomeAluno + ": "))
        notaExerT = (notaExer3 + notaExer2 + notaExer1)/3
        print("a media das notas de exercícios desse aluno foi: " + str(notaExerT))
        notaProj = float(input("Nota do projeto pratico de " + nomeAluno + ": "))
        print("Professor, você deseja alterar os parametros para o calculo da média?")
        print("1 - sim, modificar ou 2 - não, manter padrão")
        alt1 = input("(a media atual é composta por: 60% das provas, 30% do projeto e 10% dos exercícios individuais) ")
        medilinda = 0
        if alt1 == "2":
            mediaFInd = 0.6*mediaProvas + 0.3*notaProj + 0.1*notaExerT
            print("prof, " + nomeProf + ", a média do aluno " + nomeAluno + " nesse semestre foi " + str(mediaFInd))
            notasL.append(mediaFInd)
            medilinda = mediaFInd
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
        if alt1 == "1":
            print("defina os pesos em porcentagem para os seguintes parametros:")
            pesoProva = float(input("Peso para a media das provas: "))/100
            pesoPratic = float(input("peso para o projeto prático: "))/100
            pesoExer = float(input("peso para as atividades individuais: "))/100
            mediaMod = pesoProva*mediaProvas + pesoPratic*notaProj + pesoExer*notaExerT
            print("professor, " + nomeProf + ", a média do aluno " + nomeAluno + " nesse semestre foi " + str(mediaMod))
            notasL.append(mediaMod)
            medilinda = mediaMod
            if mediaMod >= 6:
                print(nomeAluno + " é elegivel para aprovação")
            elif (mediaMod >= 4) and (mediaMod < 6):
                print(nomeAluno + " é elegivel para recuperação")
            else:
                print(nomeAluno + " foi reprovado por nota")
                apRep.append("REPROVADO")
                opic = input("Deseja calcular a aprovação de outro aluno? 1 - sim ou 2 - não: ")
                zopic = opic
        if perguntarPresenca == True:
            print(nomeProf + ", para definir a aprovação ou não do aluno é necessário verificar o % de presença do mesmo")
            print("um aluno cuja presença seja maior ou igual a 75% do período de aulas é elegivel para aprovação")
            aulasRedef = "2"
            print("por padrão existem 26 semanas em um semestre com 6 aulas por semana totalizando uma qtd N de 156 aulas")
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
    if (zopic == "2") and (opic == "2"):
        qtddAlunos = 0
        # for aluno in alunosL:
        #    print(aluno + ' - nota : ' + notasL[qtddAlunos] + ' presenca -> ' + presenca[qtddAlunos])
        #    qtddAlunos = qtddAlunos +1

        # aluNotCon = [item for sublist in zip(alunosL, notasL, presenca, apRep) for item in sublist]
        print("===>RELATÓRIO FINAL<===")
        print("Professor, " + nomeProf + " os resultados dos aprovados e reprovados de hoje foram: ")
        for aluno in alunosL:
            print(aluno + ' - nota : ' + str(notasL[qtddAlunos]) + ' presenca -> ' + presenca[qtddAlunos] + apRep)
            qtddAlunos = qtddAlunos + 1
