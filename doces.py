# luana monteiro fabrica de doces
def cadastrar(matriz, para1, para2=0.0, para3='', para4=''):
    lista = [para1, para2, para3, para4]
    matriz.append(lista)


def existe(matriz, para1, coluna=0):
    for al in range(len(matriz)):
        if matriz[al][coluna] == para1:
            return True
    return False


def existe_lista(lista, para1):
    for ej in range(len(lista)):
        if lista[ej] == para1:
            return True
    return False


def onde_ta_lista(lista, para1):
    if existe_lista(lista, para1) is True:
        return lista.index(para1)


def onde_ta(matriz, para1, coluna=0):
    if existe(matriz, para1, coluna) is True:
        return matriz.index(para1)

def deu_ruim():
    print('é... não deu certo')
    pass


print(f"0 - sair \n"
      f"1 - cadastrar um doce\n"
      f"2 - listar doces por categoria\n"
      f"3 - cadastrar clientes\n"
      f"4 - listar os clientes \n"
      f"5 - registrar uma venda\n"
      f"6 - listar vendas realizadas\n"
      f"7 - apagar um doce sem vendas do sistema\n"
      f"8 - listar bala mais caro\n"
      f"9 - listar vendas de um cliente por pesquisa\n"
      f"10 - cadastrar faturas pagas\n")

opc = -5
cadDoce = []
cadCli = []
cadVendas = []
dicCat = {}
while opc != 0:
    opc = int(input(f"digite opção desejada: "))
    if opc == 1:
        doce = input(f"Nome do doce: ")
        if existe(cadDoce, doce, 0) is True:
            print(f"Nome ja cadastrado, escolha outro nome")
            opc = 1
        else:
            valor = float(input(f"Valor de {doce}: "))
            if valor < 10:
                print(f"Valor muito baixo, insira um novo valor")
                opc = 1
            else:
                cat = input(f"Categoria de {doce}: ")
                cadastrar(cadDoce, doce, valor, cat)
                print(f"{doce} cadastrado com sucesso!")
    elif opc == 2:  # pedir ajuda
        for i in range(len(cadDoce)):
            if cadDoce[i][2] not in dicCat.keys():
                dicCat[cadDoce[i][2]] = []
                dicCat[cadDoce[i][2]].append(cadDoce[i][0])
            else:
                dicCat[cadDoce[i][2]].append(cadDoce[i][0])
        for chave in dicCat.keys():
            print(f"doces na categoria {chave}:\n"
                  f"{str(dicCat[chave])} ")
    elif opc == 3:
        nome = input("digite o nome do cliente: ")
        if existe(cadCli, nome, 0) is True:
            print(f"Nome ja cadastrado")
        else:
            cadastrar(cadCli, nome)
    elif opc == 4:
        print("Os clientes são: ")
        for i in range(len(cadCli)):
            print(f"{cadCli[i][0]}")
    elif opc == 5:
        fatTot = 1
        clicompra = input(f"Cliente que faz a compra: ")
        if existe(cadCli, clicompra, 0) is False:
            print(f"Cliente não cadastrado")
        else:
            qtdCompra = int(input(f"Numero de itens comprados: "))
            for i in range(qtdCompra):
                qDoce = input(f"doce nº{i} comprado por {clicompra}: ")
                if existe(cadDoce, qDoce, 0) is False:
                    print(f"O doce {qDoce} não foi cadastrado")
                    break
                else:
                    print(f"Preços dos Doces\n")
                    for k in range(len(cadDoce)):
                        print(cadDoce[k])
                    qnts = int(input(f"Qnts unidades de {qDoce} foram adquiridas: "))
                for j in range(len(cadDoce)):
                    if qDoce == cadDoce[j][0]:
                        fatTot = qnts * cadDoce[j][1]
                    for e in range(len(cadCli)):
                        if clicompra == cadCli[e][0]:
                            clicompra[e][1] += fatTot
                cadastrar(cadVendas, qnts, fatTot, qDoce, clicompra)
    elif opc == 6:
        print(f"Vendas realizadas\n"
              f"quantidade , valor total, nome dos doces, nome do comprador")
        for i in range(len(cadVendas)):
            print(cadVendas[i])
    elif opc == 7:
        qmApagar = input(f"Doce para apagar: ")
        if existe(cadVendas, qmApagar, 2) is True:
            print(f"ja foi cadastrada venda para o doce, impossivel apagar")
        categoria = ''
        apagar = ''
        for ja in range(len(cadDoce)):
            if cadDoce[ja][0] == qmApagar:
                categoria = cadDoce[ja][2]
                apagar = cadDoce[ja][0]
                cadDoce[ja].remove(apagar)
        if dicCat is True:
            dicCat.pop(categoria, qmApagar)

        print(cadDoce)
        print(dicCat)