# exercício 19 - Luana Monteiro ap1s1
print("===RENDIMENTOS===")
opcao = 1
while opcao != 2:
    odomInicio = float(input("qual a medição do odometro no inicio do dia? "))
    odomFim = float(input("Qual a medição do odometro no fim do dia? "))
    litros = float(input("Quantos litros de combustivel foram gastos ao todo? "))
    total = float(input("Qual valor final recebido por todas as corridas? "))
    varKm = odomFim - odomInicio
    eficiencia = round(varKm/litros)
    valorKm = 2.50/eficiencia
    lucro = round(total - (varKm * valorKm))
    msgFim = "O lucro do dia de hoje foi " + str(lucro) + " o carro fez " + str(eficiencia) + " km/l"
    if lucro <= 100.00:
        print(msgFim + " o lucro foi inferior a meta de R$ 100.00, o desempenho deve ser melhorado")
    else:
        print(msgFim)
    opcao = int(input("Reiniciar programa? 1 - sim ou 2 - não "))
