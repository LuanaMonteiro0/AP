# exercício 8 - Luana Monteiro ap1s1
n = int(input("Qual a quantidade de pessoas no grupo? "))
caboAgente = 1
somador = 0
while caboAgente <= n:
    idade = int(input("Qual a idade do " + str(caboAgente) + "º individuo? "))
    caboAgente = caboAgente + 1
    somador = idade + somador
media = round(somador/n, 2)
if media <= 25:
    print("A media das idades é: " + str(media) + "\nA turma é jovem")
elif 26 <= media <= 60:
    print("A media das idades é: " + str(media) + "\nA turma é adulta")
else:
    print("A media das idades é: " + str(media) + "\nA turma é Idosa")
