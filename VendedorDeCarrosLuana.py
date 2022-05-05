# Exercício 13 - Luana Monteiro ap1s1
modeloBarato = []
valoresBaratos = []
comisBarato = 0
modeloMedio = []
valoresMedios = []
modeloCaro = []
valoresCaros = []
comisCaroMedios = 0
ondeTa = 0
qntsCarros = int(input("Quantos Carros foram vendidos hoje? "))
chega = 1
while chega <= qntsCarros:
    mod = input("Qual o modelo do " + str(chega) + "º carro? ")
    val = float(input("Qual o valor do " + str(chega) + "º carro? "))
    chega += 1
    if val <= 10000.00:
        modeloBarato.append(mod)
        valoresBaratos.append(val)
        comis = val * 0.1
        comisBarato += comis
    elif 20000.00 < val <= 30000.00:
        modeloMedio.append(mod)
        valoresMedios.append(val)
        comis = val * 0.11
        comisCaroMedios += comis
    else:
        modeloCaro.append(mod)
        valoresCaros.append(val)
        comis = val * 0.11
        comisCaroMedios += comis
comisFim = comisBarato + comisCaroMedios
carrosMedios = len(modeloMedio)
listaTdsValores = valoresCaros + valoresMedios + valoresBaratos
listaTdsModelos = modeloCaro + modeloMedio + modeloBarato
carroMcaro = None
for carro in listaTdsValores:
    if carroMcaro is None or carro > carroMcaro:
        carroMcaro = carro
        ondeTa = listaTdsValores.index(carroMcaro)
somaTd = sum(listaTdsValores)
mediaVal = somaTd / len(listaTdsValores)
print("A) A comissão total final recebida pelo vendedor foi de " + str(round(comisFim, 2)) + " reais.")
print("B) O modelo de carro mais caro é: " + str(listaTdsModelos[ondeTa]))
print("   O valor desse carro é: " + str(carroMcaro))
print("C) Os carros de valor maior que 20k e menores ou iguais á 30k são " + str(carrosMedios))
print("D) O preço médio dos carros vendidos é: " + str(round(mediaVal, 2)) + " reais.")
