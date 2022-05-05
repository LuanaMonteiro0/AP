#Tarefa 1 - Ads modulo 1 - programa de calculo de nota
print("=====CALCULADORA DE NOTAS=====")
nomeProf = input("Professor(a), qual o seu nome? ")
print("===DADOS===")
nomeAluno = input("Qual o nome do(a) aluno(a) cuja nota será calculada? ")
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
alt1 = 1
print()


