# exercício 17
# Escrever um programa que permita ao usuário digitar o dia e mês de seu
# aniversário e a data de hoje (dia e mês); em seguida, o programa deve calcular
# quantos dias faltam entre a data de hoje e a data do próximo aniversário. Suponha
# todos os meses com 30 dias.
opcao = 1
while opcao != 2:
    print("O ano simulado tem 360 dias")
    dia = int(input("Digite o dia de hoje de 1 a 30 "))
    mes = int(input("Digite o mes atual de 1 a 12 "))
    niver = int(input("Digite o dia do seu aniversário 1 a 30 "))
    nMes = int(input("Digite o mes do seu aniversário de 1 a 12 "))
    somaDiasAtual = (mes - 1)*30 + dia
    somaDiasNiver = (nMes - 1) * 30 + niver
    if somaDiasNiver > somaDiasAtual:
        print("O aniversario vai ocorrer")
        diaMesAtual = (30 - dia)
        diasEntreMeses = (nMes - mes - 1) * 30
        somaDias = diaMesAtual + diasEntreMeses + niver
        print("Faltam " + str(somaDias) + " dias para seu aniversário")
    elif somaDiasNiver == somaDiasAtual:
        print("Feliz Aniversário!")
    else:
        print("o aniversário ja ocorreu")
        diaMesAtual = (30 - dia)
        diasEntreMeses = ((nMes - 1) + (12 - mes)) * 30
        somaDias = diaMesAtual + diasEntreMeses + niver
        print("Faltam " + str(somaDias) + " dias para seu aniversário")
    opcao = int(input("Reiniciar programa? 1 -sim ou 2 - não "))
