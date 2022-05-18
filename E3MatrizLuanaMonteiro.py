#  Luana monteiro ex 3
mat = []
for i in range(8):
    linha = []
    for j in range(8):
        if i % 2 == 0:
            if i % 2 == 0 and j % 2 == 0:
                linha.append(0)
            else:
                linha.append(1)
        else:
            if i % 2 == 1 and j % 2 == 0:
                linha.append(1)
            else:
                linha.append(0)
    mat.append(linha)

for i in range(8):
    print(mat[i])
