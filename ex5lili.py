# lista 3 ex 5 – Luana Monteiro

from random import randint
pessoas = []
quantidade = 0
vei6069 = 0
vei7079 = 0
veimais80 = 0
zero49 = 0
cincoenta9 = 0
xovens = 0
idosos = 0
creonca = 0
while quantidade != 50:
    idade = randint(1, 100)
    pessoas.append(idade)
    quantidade += 1
    if quantidade == 50:
        break

for item in pessoas:
    if item <= 20:
        xovens += 1
    elif item >= 60:
        idosos += 1
        if (item >= 60) and (item <= 69):
            vei6069 += 1
        elif (item >= 70) and (item <= 79):
            vei7079 += 1
        elif item >= 80:
            veimais80 += 1
    if item <= 49:
        zero49 += 1
    if item <= 10:
        creonca += 1
    elif (item >= 50) and (item <= 59):
        cincoenta9 += 1

# print(f"As idades são {pessoas}")  # debug
# print(f"Foram geradas {len(pessoas)} idades")  # debugg
print(f"A) Existem {xovens} jovens no grupo - {round(xovens/50 * 100, 3)}%")
print(f"B) Existem {idosos} idosos no grupo - {round(idosos/50 * 100, 3)}%")
print(f"c) Existem {creonca} crianças que não tem risco de morte"
      f" por serem menores de 10 anos - {round(creonca/50 * 100, 3)}%")
print(f"D) Existem {zero49} pessoas entre 0 e 49 anos com 1% de mortalidade \n"
      f"   Existem {cincoenta9} pessoas entre 50 e 59 anos com 1,3% de mortalidade \n"
      f"   Existem {vei6069} pessoas entre 60 e 69 anos com 3,6% de mortalidade \n"
      f"   Existem {vei7079} pessoas entre 70 e 79 anos com 8% de mortalidade \n"
      f"   Existem {veimais80} pessoas com mais de 80 anos com 14,8% de mortalidade \n")
conta = (0.01 ** (zero49 - creonca)) * (0.013 ** cincoenta9) * (0.036 ** vei6069) * (0.08 ** vei7079) * (0.148 ** veimais80)
contaOnlyveio = (0.036 ** vei6069) * (0.08 ** vei7079) * (0.148 ** veimais80)

# print(f"{conta * 100}%")
# print(f"{contaOnlyveio * 100}%")
print(f"D) Existe {conta * 100}% de chance de alguém no grupo todo morrer (descontando os menores de 10 anos)\n"
      f"   Existe {contaOnlyveio * 100}% de chance de algum idoso morrer (maior que 60 anos)\n")
