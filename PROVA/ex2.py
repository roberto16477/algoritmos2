import numpy as np

V = []
N = 5
inverso = np.zeros(N)

for i in range(N):
    V.append(int(input("Informe um valor: ")))

for j in range(N):
    aux = (N-1)-j
    inverso[aux] = int(V[j]-2*V[j])
    



print(V)
print(inverso)