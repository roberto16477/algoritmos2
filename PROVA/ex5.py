V = []
M = []
R = []
N = 3

for i in range(N):
    V.append(int(input("Informe um valor para o vetor: ")))

for l in range(N):
    lista = []
    for c in range(N):
        lista.append(int(input("Informe um valor para a matriz: ")))
    M.append(lista)

for l in range(N):
    linha = []
    for c in range(N):
        linha.append(V[l] * M[c][l])
    R.append(linha)

print("Vetor: ", V)

print("Matriz Inicial: ")
for num in M:
    print(num)

print("Matriz Resultante: ")
for num in R:
    print(num)
