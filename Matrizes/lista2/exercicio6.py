N = 5
lista = []
M = [[],[],[],[],[]]

for i in range(N):
    lista.append(int(input(f"Informe o {i+1}o valor: ")))

for i, l in enumerate(M):
    for c in range(len(M)):
        l.append(int(input(f"Informe {i},{c}: ")))

R = []
for l in range(N):
    linha = []
    for c in range(N):
        linha.append(lista[l] * M[l][c])
    R.append(linha)

print(lista)
print(M)
print(R)