M = []
N = 3
#preenche sem numpy
for i in range(N):
    lista = []
    for j in range(N):
        lista.append(int(input("Informe um valor para a matriz: ")))
    M.append(lista)

print(M)
