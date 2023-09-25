import numpy as np

N = 4

M1 = np.zeros((N, N))

for l in range(N):
    for c in range(N):
        M1[l][c] = int(input(f"Informe valor para lin {l}, col {c}:"))

a = int(input("Informe o multiplicador: "))

lista = []

for l in range(N):
    for c in range(N):
        lista.append(a * M1[l][c])

print(lista)