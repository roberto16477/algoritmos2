import numpy as np

N = 5

M1 = np.zeros((N, N))

for l in range(N):
    for c in range(N):
        M1[l][c] = int(input(f"Informe valor para lin {l}, col {c}:"))

sl = []
for l in range(N):
    soma = 0
    for c in range(N):
        soma+=M1[l][c]
    sl.append(soma)

sc = []
for c in range(N):
    soma = 0
    for l in range(N):
        soma+=M1[l][c]
    sc.append(soma)

print(sl)
print(sc)