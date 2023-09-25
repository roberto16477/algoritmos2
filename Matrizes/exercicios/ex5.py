M = []
N = 3
soma = 0
somaDP = 0

for l in range(N):
    lista = []
    for c in range(N):
        lista.append(int(input("Informe um valor: ")))
    M.append(lista)

for i in range(N):
    for j in range(N):
        if j == 1:
            soma = soma + M[i][j]
        if i == j:
            somaDP = somaDP + M[i][j]



for item in M:
    print(item)

print("A soma dos valores da Segunda coluna é: ", soma)
print("A soma da diagonal principal é: ", somaDP)
