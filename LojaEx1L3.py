# Exercício 1 lista 3 - Luana Monteiro Ap1s1
preco = 1
nome = ""
qtd = 0
cat = ""
contLuxo2k = 0
contLuxoTd = 0
somaLuxoTd = 0
prodCaro = 0
nomeProdCaro = ""
totalProd = 0
qtdBaratinho = 0
prodBarato = 50000
nomeBarato = ""
while preco != 0:
    preco = float(input("Qual o preço a ser cobrado pelo produto? "))
    if preco != 0:
        nome = input("Qual produto deve ser cadastrado? ")
        qtd = int(input("Qual a quantidade de produtos? "))
        cat = input("Qual a categoria do produto? L = luxo e C = comum: ")
        totalProd += 1
        if cat == "L" and preco <= 2000.00:
            contLuxo2k += 1
        if cat == "L":
            contLuxoTd += 1
            somaLuxoTd += preco
        if prodCaro <= preco and qtd <= 50:
            prodCaro = preco
            nomeProdCaro = nome
        if 100.00 < preco <= 200.00:
            qtdBaratinho += 1
        if prodBarato >= preco and cat == "C":
            prodBarato = preco
            nomeBarato = nome
    else:
        print('obrigado')

mediaLx = somaLuxoTd/contLuxoTd
porcento = qtdBaratinho * 100 / totalProd
print("A qtdade de produtos de luxo com o preço menor que 2k é " + str(contLuxo2k))
print("A media do preço dos produtos de luxo é: " + str(mediaLx))
print("O nome do produto mais caro com quantidade < 50 é: " + nomeProdCaro)
print("A porcentagem de produtos que custa entre 100 e 200 é: " + str(porcento) + "%")
print("O nome do produto comum mais barato é: " + nomeBarato)
