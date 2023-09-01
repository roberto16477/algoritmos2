import numpy as np

n = 5
v = np.zeros(n)
soma = 0

for i in range(n):
    v[i] = float(input("Informe um valor: "))
    soma = soma + v[i]

#somaaut = v.sum()
#print(v)
print("A soma dos valores do vetor é: ", soma)
#print("Soma com função: ", somaaut)
