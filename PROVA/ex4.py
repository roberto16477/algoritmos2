M = []
N = 6


for l in range(N):
    lista = []
    for c in range(N):
        lista.append(int(input("Informe um valor para a matriz: ")))
    M.append(lista)

#for num in M:
 #   print(num)

for i in range(N):
    auxl = M[1][i]
    M[1][i] = M[4][i]
    M[4][i] = auxl

for i in range(N):
    aux = M[i][3]
    M[i][3] = M[i][5]
    M[i][5] = aux

print("Matriz após as alterações: ")
for num in M:
    print(num)
