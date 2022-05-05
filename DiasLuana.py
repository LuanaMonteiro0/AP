# Exercício 16 - Luana Monteiro ap1s1
print("O ano simulado tem 360 dias")
dias = list(range(1, 31))
dia = int(input("Digite um dia de 1 a 30 "))
dEscolhido = dia - 1
varDias1 = (len(range(1, dEscolhido))) + 2
mes = int(input("Digite um mes de 1 a 12 "))
totDiasAntesFim = 360 - ((mes - 1) * 30 + varDias1)
print("Faltam " + str(totDiasAntesFim) + " dias antes do fim do ano")
print("Já se passaram " + str(varDias1) + " dias")

# diaAtual = int(input("digite o dia atual: "))
# mesAtual = int(input("Digite o mes atual: "))
# diasNoMesAtual = 30*(12 - mesAtual)
# total = diasNoMesAtual +diasNosMeses
# print("qtd de dias que faltam: " + str(total))
