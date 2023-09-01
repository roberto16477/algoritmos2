import numpy as np
n = 5

vetor = np.zeros(n)

for i in range(n):
    vetor[i] = int(input("Informe um valor: "))

for i in range(n):
   # print(f'V[{i}] = {vetor[i]}')
    print("Posição [", i,"] = ", vetor[i])

#o ultimo for exibe os valores do vetor e seu índice
