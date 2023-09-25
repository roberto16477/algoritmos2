import numpy as np

N = 3
M = np.zeros((N, N))


for i in range(N):
    for j in range(N):
        M[j][i]  = input(f'Digite o valor da coluna {i} e linha {j}:  ')


for x in M:
    print(x, end='\n')