n = int(input('qual o valor de n? '))
eprimo = 6
for id1 in range(2, n+1):
    for id2 in range(2, id1):
        if n % id2 == 0:
            eprimo = 2
        else:
            eprimo = 1
    if eprimo == 1:
        print(id1)
