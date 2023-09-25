N = 5
M = []
soma = 0

for l in range(N):
    lista = []
    for c in range(N):
        lista.append(int(input("Informe um valor: ")))
    M.append(lista)

for num in M:
    print(num)

for i in range(N):
    for j in range(N):
        if i == 3:
            soma = soma+M[i][j]


print("A soma da linha 4 é: ", soma)
