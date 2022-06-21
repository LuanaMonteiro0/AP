# lUANA MONTEIRO AP1S1

def abrir_arquivo(nomearq, matriz):
	arquivo = open(nomearq, 'r')
	for linha in arquivo:
		linha = linha.replace('\n', '')
		linha = linha.replace('\t', ',')
		dados = linha.split(',')
		matriz.append(dados)
	arquivo.close()
	return matriz


def exibir_dados(matriz):
	for ki in range(len(matriz)):
		print(matriz[ki])


def vago(item):
	if item == "0":
		return True
	else:
		return False


def ta_vago(matriz, linha, coluna):
	for li in range(len(matriz)):
		if li == linha:
			for oi in range(len(matriz)):
				if oi == coluna:
					return vago(matriz[li][oi])


def covidar(matriz):
	for lin in range(len(matriz)):
		for col in range(len(matriz)):
			if matriz[lin][col] == "X":
				if matriz[lin][col + 1] == "0":
					matriz[lin][col + 1] = "B"
				if matriz[lin][col - 1] == "0":
					matriz[lin][col - 1] = "B"


def atualiza_arq(matriz, arquivo):
	arq = open(arquivo, "w")
	for linhaa in matriz:
		matriz[linhaa] = matriz[linhaa].replace(',', '\t')
		arq.write(matriz[linhaa] + "\n")
	arq.close()


def conta_itens(matriz):
	compraaa = 0
	covd = 0
	scom = 0
	for linhs in range(len(matriz)):
		for colona in range(len(matriz)):
			if matriz[linhs][colona] == "X":
				compraaa += 1
			if matriz[linhs][colona] == "B":
				covd += 1
			if matriz[linhs][colona] == "0":
				scom += 1
	return compraaa, covd, scom

dicLugares = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13}
caderinhas = []
crientes = []
cine = "cine.csv"
print(f"===MENU===\n"
      f"0 - sair\n"
      f"1 - mapa de poltronas\n"
      f"2 - Realizar venda de lugares\n"
      f"3 - Relatório\n")
abrir_arquivo(cine, caderinhas)
opc = -15
while opc != 0:
	opc = int(input(f"Opção: "))
	if opc == 1:
		print(f"Os lugares disponiveis para o filme são: ")
		exibir_dados(caderinhas)
	elif opc == 2:
		nomeCli = input(f"Nome do cliente: ")
		if nomeCli not in crientes:
			lugares = int(input(f"Quantos lugares {nomeCli} comprará?: "))
			comprados = []
			while lugares > 4 or lugares < 0:
				lugares = int(input(f"Numero invalido. {nomeCli} comprará quantos lugares?: "))
			while len(comprados) != lugares:
				ondeTar = input(f"Digite a fileira e coluna para {len(comprados)+1}º lugar (ex: 1A): ")
				lenha = int(ondeTar[0])
				coluuna = dicLugares[ondeTar[1].upper()]
				if ta_vago(caderinhas, lenha, coluuna) is True:
					print(f"Cadeira adquirida!")
					comprados.append(ondeTar)
					caderinhas[lenha][coluuna] = "X"
				else:
					print(f"Cadeira ocupada")

			if len(comprados) == lugares:
				nomeCli = [nomeCli]
				crientes.append(nomeCli)
				crientes.append(comprados)
				covidar(caderinhas)
				atualiza_arq(caderinhas, cine)
	elif opc == 3:
		compra, covid, sVenda = conta_itens(caderinhas)
		print(f"RELATÓRIO\n"
		      f"Cadeiras compradas: {compra}\n"
		      f"Cadeiras empenhadas (covid): {covid}\n"
		      f"Cadeiras sem venda: {sVenda}")
