# exercício 6 - Luana
opcao = 9
while opcao != 2:
    print("===AZULEJOS===")
    cm = float(input("Qual o comprimento da sua cozinha? "))
    lr = float(input("Qual a largura da sua cozinha? "))
    ah = float(input("Qual a altura da sua cozinha? "))

    paredeApenas = int(input("Calcular para: 1 - apenas paredes, 2 - paredes e chão/teto ou 3 - todos?"))
    total = 0
    if paredeApenas == 1:
        total = (2*(cm*ah) + 2*(lr*ah))/2
    if paredeApenas == 2:
        total = (2*(cm*ah) + 2*(lr*ah) + (cm*lr))/2
    if paredeApenas == 3:
        total = (2*(cm*ah) + 2*(lr*ah) + 2*(cm*lr))/2
    print("O total de caixas de azulejos que serão utilizadas são: " + str(total))
    opcao = int(input("repetir? 1 - sim ou 2 - não "))

