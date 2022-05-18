# Vendas Luana Monteiro

print(f"=====LOJA DE ELETRONICOS=====")
opc = -1
inventario = []
pVendidos = []
valGasto = []
#  CADASTRO DE PRODUTOS:
print(f"===MENU INICIAR=== \n"
      f"0- Sair"
      f"1- Cadastrar produtos \n"
      f"2- Listar produtos \n"
      f"3- Listar produtos detalhadamente \n"
      f"4- Cadastrar vendas \n"
      f"5- Relatório de vendas \n"
      f"6- Relatório por cliente \n"
      f"7- Cliente com mais aquisições \n"
      f"8- Faturamento final (valor total e valor do imposto a ser pago) \n"
      f"9- Produto mais vendido \n")
while opc != 0:
    opc = int(input("Qual serviço a ser utilizado?"))
    if opc == 1:
        informacoes = []
        print(f"Cadastrar produto")
        nome = input("Qual o nome do produto? ")
        valor = float(input(f"Qual o valor do produto {nome}? "))
        estoque = int(input(f"Quantas unidades de {nome} estão no estoque? "))
        informacoes.append(nome)
        informacoes.append(valor)
        informacoes.append(estoque)
        inventario.append(informacoes)
    elif opc == 2:
        print("Nome dos produtos")
        for i in range(len(inventario)):
            print(f"O produto #{i+1} é {inventario[i][0]}")
    elif opc == 3:
        print("Detalhamento dos produtos")
        for i in range(len(inventario)):
            print(f"O produto #{i+1} é {inventario[i][0]} \n"
                  f"O valor é {inventario[i][1]} reais \n"
                  f"O estoque disponivel é {inventario[i][2]} \n")
    elif opc == 4:
        print("Cadastro de vendas")
        lista = []
        nomeProd = input(f"Qual produto foi comprado? ")
        existe = False
        for i in range(len(inventario)):
            if nomeProd == inventario[i][0]:
                existe = True
            if existe is False:
                print(f"Produto {nomeProd} não cadastrado")
                sopc = int(input("Deseja cadastrar o produto? 1 - sim ou 2 - não"))
                if sopc == 1:
                    opc = 1
                else:
                    print(f"O produto não será cadastrado!")
                    opc = -1
            elif existe is True:
                nomeCli = input(f"Qual o nome do cliente? ")
                qntComprada = int(input(f"Qual a quantidade que {nomeCli} adiquiriu de {nomeProd}?"))
                if qntComprada >= inventario[i][2]:
                    print(f"Quantidade disponivel em estoque!"
                          f"Cadastro de venda concluido com sucesso")
                    valorGasto = inventario[i][1] * qntComprada
                    lista.append(nomeProd)
                    lista.append(qntComprada)
                    lista.append(nomeCli)
                    inventario[i][2] -= qntComprada
                    pVendidos.append(lista)
                    valGasto.append(valorGasto)
                else:
                    print(f"Quantidade indisponivel para compra\n"
                          f"Cadastro de venda cancelado\n")
    elif opc == 5:
        print("Relatório de vendas")
        for i in range(len(pVendidos)):
            print(f"A venda #{i+1} foi do produto {pVendidos[i][0]} \n"
                  f"A quantidade comprada foi {pVendidos[i][1]} \n"
                  f"O cliente que adiquiriu é {pVendidos[i][2]} \n"
                  f"O valor gasto pelo cliente {valGasto[i]}")
    elif opc == 6:
        cliente = input("Qual produto deve ser buscado? ")
        entrei = False
        for i in range(len(pVendidos)):
            if cliente == pVendidos[i][2]:
                print(f"Nome do produto: {pVendidos[i][0]}\n"
                      f"quantidade: {pVendidos[i][1]}\n"
                      f"Cliente: {pVendidos[i][2]}\n")
                entrei = True
        if entrei is False:
            print(f"Não houveram vendas para clientes com esse nome")
    elif opc == 7:
        print("Cliente que mais gastou")
        maisComprado = 0
        nomeMaisCompra = ""
        for i in range(len(pVendidos)):
            if maisComprado < pVendidos[i][1]:
                maisComprado = pVendidos[i][1]
                nomeMaisCompra = pVendidos[i][2]
        print(f"O cliente que comprou mais produtos foi {nomeMaisCompra}")
    elif opc == 8:
        valTot = 0
        for i in range(len(valGasto)):
            valTot += valGasto[i]
        taxa = valTot * 0.2
        valFinal = valTot - taxa
        print(f"O valor total obtido foi {valTot}"
              f"O valor do imposto é {taxa}"
              f"O valor final dos lucros é {valFinal}")
    elif opc == 9:
        maisVendido = ""
        pmaisv = 0
        for i in range(len(pVendidos)):
            if pmaisv < pVendidos[i][1]:
                pmaisv = pVendidos[i][1]
                maisVendido = pVendidos[i][0]
        print(f"O produto mais vendido de hoje foi {maisVendido}")
