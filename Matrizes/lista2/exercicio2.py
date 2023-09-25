M = []
N = 5


for l in range(N):
    lista = []
    for c in range(N):
        lista.append(int(input("Informe um valor para a matriz: ")))
    M.append(lista)


print("Matriz Original:")
for num in M:
    print(num)

for i in range(N):
    auxl = M[2][i]
    M[2][i] = M[4][i]
    M[4][i] = auxl

for i in range(N):
    aux = M[1][i]
    M[1][i] = M[i][4]
    M[i][4] = aux

print("Alterada: ")

for valor in M:
    print(valor)

