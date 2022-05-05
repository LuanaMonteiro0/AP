# exercício 3
# le idade e determina se é eleitor obrigatorio, facultativo (entre 16 e 18 ou maior que 65) ou não eleitor

nome = input("digite o nome do possível eleitor: ")
idade = int(input("digite a idade do possível eleitor: "))

if idade < 16:
    print("Não eleitor! ");
elif (idade >= 18) and (idade < 65):
    print("Eleitor obrigatório! ")
elif ((idade >= 16) and (idade < 18)) or (idade >= 65):
    print("Voto Facultativo! ")
