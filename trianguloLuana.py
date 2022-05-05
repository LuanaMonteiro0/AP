# exercício 12 Luana Monteiro = corrigido com bool e isosceles
opcao = 8  # opção para definir repetição do codigo (tenho raiva de ficar apertando play dnv)
while opcao != 2:
    print("==TRIANGULOS==")
    seraTri = True
    pVal = float(input("Qual o primeiro lado do triangulo? "))
    sVal = float(input("Qual o segundo lado do triangulo? "))
    tVal = float(input("Qual o terceiro lado do triangulo? "))
    if (pVal < sVal + tVal) and (sVal < tVal + pVal) and (tVal < pVal + sVal):
        seraTri = True  # forma triangulo
    else:
        seraTri = False  # não forma triangulo
    if seraTri:
        if (pVal != sVal) and (sVal != tVal) and (tVal != pVal):
            print("Forma um triangulo escaleno")
        elif (tVal == pVal) or (sVal == tVal) or (pVal == sVal):
            print("Forma um triangulo isosceles")
        else:
            print("Forma um triangulo equilatero")

    else:
        print("Não Forma um triangulo")

    opcao = int(input("Deseja reiniciar o programa? 1 - sim ou 2 - não: "))
