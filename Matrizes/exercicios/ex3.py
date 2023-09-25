N = 3
M = []
DP = []

for i in range(N):
    lista = []
    for j in range(N):
        lista.append(int(input("Informe um valor: ")))
    M.append(lista)

for k in M:
    print(k)

for l in range(N):
    for c in range(N):
        if l == c:
            DP.append(M[l][c])

print("Os valores da diagonal principal são: ", DP)