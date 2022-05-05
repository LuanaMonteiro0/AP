# exercício do imc

print("===CALCULADORA DE IMC===")
nome = input("qual o nome do indivíduo? ")
txt1 = input("Qual o peso de " + nome + "? ")
txt1 = txt1.replace(",", ".")
peso = float(txt1)
txt2 = input("Qual a altura de " + nome + "? ")
txt2 = txt2.replace(",", ".")
altura = float(txt2)
IMC = peso/altura**2
print(str(IMC) + " é o IMC de " + nome)
if IMC < 18.5:
    print(nome + " está abaixo do peso")
elif (IMC >= 18.5) and (IMC < 25):
    print(nome + " está com peso normal")
elif (IMC >= 25) and (IMC < 30):
    print(nome + " está acima do peso")
else:
    print(nome + " é obeso")
