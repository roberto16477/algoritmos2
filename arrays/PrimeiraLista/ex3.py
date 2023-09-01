import numpy as np

n = 5
v = np.zeros(n)
soma = 0
media = 0

for i in range(n):
    v[i] = float(input("Informe um valor: "))
    soma = soma + v[i]

#mediaaut = v.mean()
media = (soma/n)

print("A média dos valores é: ", media)
#print("Aut é: ", mediaaut)
