# Faça um programa para informatizar o cadastro dos pacientes em um hospital. Você deve
# cadastrar os pacientes com as seguintes informações: nome, idade, sexo (M ou F) e peso. Após
# terminado o cadastro, perguntar se o usuário deseja cadastrar mais alunos. Caso ele responda “sim”
# outro cadastro deve ser efetuado. Do contrário, deve ser informado:
# - o nome do paciente mais velho e com peso maior que 50 quilos.
# - peso médio dos pacientes do sexo feminino com mais de 30 anos.
# - a quantidade de pacientes do sexo masculino ou com idade menor que 45 anos.
# - o percentual de pacientes (masculino ou feminino) que são idosos (mais de 59 anos).

print("===CADASTROS HOSPITALARES===")
nome = ''
idade = 0
sexo = "X"
peso = 0
continuar = "sim"
maisVelho = ""
velho = 0
cntPaci = 0
cntpaciFmaistrinta = 0
pesopaciFmaistrinta = 0
hMenosqcinco = 0
qntVeio = 0
while continuar == "sim":
    nome = input("Qual o nome do paciente? ")
    idade = int(input("Qual a idade de " + nome + "? "))
    sexo = input("Qual o sexo biologico de " + nome + "? ")
    peso = float(input("Qual o peso de " + nome + "? "))
    cntPaci += 1
    if idade > velho and peso > 30:
        velho = idade
        maisVelho = nome
    if sexo == 'F' and idade > 30:
        cntpaciFmaistrinta += 1
        pesopaciFmaistrinta += peso
    if sexo == 'M' or idade < 45:
        hMenosqcinco += 1
    if idade > 59:
        qntVeio += 1

    continuar = input("Cadastrar novo paciente? (sim ou não) ")
print("A) O nome do paciente mais velho com mais de 50kg é: " + maisVelho)
pMedio = pesopaciFmaistrinta / cntpaciFmaistrinta
print("B) O peso medio das pacientes com mais de 30 anos é: " + pMedio)
print("C) A qnt de pacientes homens ou com menos de 45 anos é: " + hMenosqcinco)
pVeios = qntVeio * 100 / cntPaci
print("D) o percentual de idosos é de: " + str(pVeios) + "%")