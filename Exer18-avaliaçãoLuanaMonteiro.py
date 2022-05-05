# exercício 18 - luana Monteiro ap1

idade = int(input("Qual a sua idade? "))
sexo = int(input("Qual seu sexo biológico? 1 - masculino ou 2 - feminino? "))
salario = float(input("Qual seu salario? "))
if (sexo == 1) and (idade > 18):
    print("Sexo masculino, com idade maior que 18 anos")
elif (sexo == 2) and (idade > 40) and (salario > 50000.00):
    print("Sexo feminino, com salário maior que 50.000,00 e idade acima de 40 anos")
if ((sexo == 1) or (sexo == 2)) and ((idade > 20) and (idade < 30)):
    print("Sexo masculino ou feminino e idade entre 20 e 30 anos")
else:
    print("Não se encaixa em nenhuma das possibilidades anteriores")

