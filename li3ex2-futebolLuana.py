# Faça um programa para informatizar o cadastro dos jogadores de futebol em um time. Você deve
# cadastrar os jogadores com as seguintes informações: nome, idade, peso e time. Após terminado o
# cadastro, perguntar se o usuário deseja cadastrar mais jogadores. Caso ele responda “sim” outro
# cadastro deve ser efetuado. Do contrário, deve ser informado:
# - média de idade dos jogadores do “corinthians” com mais de 80 quilos.
# - o percentual de jogadores que tem menos de 20 anos
# - o nome do jogador mais novo e com peso maior que 70 quilos.
# - a quantidade de jogadores do “santos” com idade maior que 20 ou com peso menor ou igual a 65
# quilos
nome = ''
idade = 0
peso = 0
time = ''
continuar = 'sim'
cntJgdr = 0
cntCori = 0
somaCori = 0
cntMeVin = 0
jgdrMaisNv = ""
AvalMaisNv = 90
cntSantos = 0
while continuar == 'sim' or continuar == 'Sim':
    nome = input("Qual o nome do " + str(cntJgdr + 1) + "º jogador? ")
    idade = int(input("Quantos anos tem " + nome + "? "))
    peso = float(input("Quanto pesa " + nome + "? "))
    time = input("Qual o time de " + nome + "? ")
    cntJgdr += 1
    if (time == "corinthians" or time == "Corinthias") and peso > 80:
        cntCori += 1
        somaCori += idade
    if idade < 20:
        cntMeVin += 1
    if idade <= AvalMaisNv and peso > 70:
        jgdrMaisNv = nome
    if (time == "Santos" or time == "santos") and idade > 20 or peso <= 65:
        cntSantos += 1
    continuar = input("deseja continuar colocando jogadores? (sim ou não) ")
print(cntJgdr)
print(cntCori)
print(cntMeVin)
print(jgdrMaisNv)
print(cntSantos)

A = somaCori/cntCori
B = cntMeVin/cntJgdr*100

print("A) A media de idade dos jogadores do corinthians com mais de 80kg é: " + str(A))
print("B) O percentual de jogadores com menos de 20 anos " + str(B) + "%")
print("C) O jogador mais novo que pesa mais de 70 kg é: " + jgdrMaisNv)
print("D) A qtd de jogadores do “santos” com idade > 20 ou com peso menor <= 65kg é: " + str(cntSantos))



