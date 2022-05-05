# Exercício 1
primeiroNmr = int(input("Qual primeiro numero? "))
segundoNmr = int(input("Qual o segundo numero? "))
if primeiroNmr > segundoNmr:
    print(" o primeiro numero: " + str(primeiroNmr) + " é maior")
else:
    print(" o segundo numero: " + str(segundoNmr) + " é maior")

# exercício 2
primNmr = int(input("Qual primeiro numero? "))
segNmr = int(input("Qual o segundo numero? "))
terNmr = int(input("Qual o terceiro numero? "))
# if primNmr == segNmr or primNmr == terNmr or segNmr == terNmr
if primNmr > segNmr and primNmr > terNmr:
    print("o numero " + str(primNmr) + " é o primeiro e maior dos três")
elif segNmr > primNmr and segNmr > terNmr:
    print("o numero " + str(segNmr) + " é o segundo e maior dos três")
else:
    print("O numero " + str(terNmr) + " é o terceiro e maior dos três")
