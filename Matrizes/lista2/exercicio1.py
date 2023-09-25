M1 = []
M2 = []
M3 = []
N = int(input("Informe o valor quadratico das duas matrizes: "))
soma = 0

for l in range(N):
    listaM1 = []
    for c in range(N):
        listaM1.append(int(input("Informe um valor para a primeira matriz: ")))
    M1.append(listaM1)

for l2 in range(N):
    listaM2 = []
    for c2 in range(N):
        listaM2.append(int(input("Informe um valor para a segunda matriz: ")))
    M2.append(listaM2)

for i in range(N):
    for j in range(N):
        M3.append((M1[i][j])+(M2[i][j]))


print("Matriz 1: ", M1)
print("Matriz 2: ", M2)

print("A soma é: ", M3)