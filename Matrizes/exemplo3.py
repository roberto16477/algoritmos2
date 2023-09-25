matriz = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
N = len(matriz)

for i in range(N):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input("Informe um valor para a matriz: "))

print("Matriz 3x3: ", matriz)
