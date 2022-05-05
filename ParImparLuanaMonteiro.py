# Par ou impar - Luana Monteiro
print("===IMPAR OU PAR?===")
opcao = 3
while opcao != 2:
    nmr = float(input("Qual numero deseja calcular? "))
    parImpar = 3
    calc = nmr % 2
    if calc == 1:
        print("O numero é impar")
    else:
        print("O numero é par")
    opcao = int(input("Reiniciar programa? 1 - sim ou 2 - não "))
