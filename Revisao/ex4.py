M = []
N = 5

for i in range(N):
    lista = []
    for j in range(N):
        if i == j:
            lista.append(1)
        else:
            lista.append(0)
    M.append(lista)

print(M)