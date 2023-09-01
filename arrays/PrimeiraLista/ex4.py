import numpy as np

n = 5
v = np.zeros(n)
maior = 0
menor = 0

for i in range(n):
    v[i] = float(input("Insira um valor: "))
    if i == 0:
        maior = v[i]
        menor = v[i]
    else:
        if maior < v[i]:
            maior = v[i]

        if menor > v[i]:
            menor = v[i]

#maioraut = v.max()
#menoraut = v.min()

print(v)
print("O maior valor do vetor é: ", maior)
print("O menor valor do vetor é: ", menor)

#print("maior: ", maioraut, "Menor: ", menoraut)
