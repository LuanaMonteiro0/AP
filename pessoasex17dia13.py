qntsPessoas = int(input("Quantas pessoas serão cadastradas? "))
contador = 1
somidade = 0
contaBaixinhoGordo = 0
galeraAlta = 0
dezEtrintaAlta = 0
while contador <= qntsPessoas:
    idade = int(input("Qual a idade da " + str(contador) + "º pessoa?"))
    somidade += idade
    peso = float(input("Qual o peso da " + str(contador) + "º pessoa?"))
    altura = float(input("Qual a altura da " + str(contador) + "º pessoa em metros?"))
    # b) peso +90 altura -1,50
    if peso >= 90 and altura <= 1.5:
        contaBaixinhoGordo += 1
    # c) A percentagem de pessoas com idade entre 10 e 30 anos entre as pessoas
    # que medem mais de 1,90 m.
    if 10 <= idade <= 30 and altura >= 1.9:
        dezEtrintaAlta += 1
    if altura >= 1.9:
        galeraAlta += 1
    contador += 1

porcentoAltos = dezEtrintaAlta * 100 / galeraAlta
mediaidade = somidade / qntsPessoas
print("A) A media das idades dos cadastrados é: " + str(round(mediaidade)))
print("B) a quantidade de pessoas com mais de 90kg e menos de 1.50 é: " + str(contaBaixinhoGordo))
print("C) A % de pessoas maior que 10 e menor que 30 anos com mais de 1.90 é: " + str(porcentoAltos) + "%")
