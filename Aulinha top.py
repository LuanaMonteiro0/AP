# exercícios de IF
opic = "2"
while opic != "1":
    numero = int(input("digite um numero: "))
    if numero > 10:
        print("numero maior que 10")
    elif numero == 10:
        print("numero igual a 10")
    else:
        print("numero menor que 10")

    opic = input("quer calcular outro numero? 1 não 2 sim: ")
