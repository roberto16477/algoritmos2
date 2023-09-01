import numpy as np

n = 5
v = np.zeros(n)
maior = 0
menor = 0
P_maior = 0
P_menor = 0

for i in range(n):
    v[i] = float(input("Digite um valor: "))

    if i == 0:
        maior = v[i]
        menor = v[i]
        P_maior = i
        P_menor = i
    else:
        if maior < v[i]:
            maior = v[i]
            P_maior = i

        if menor > v[i]:
            menor = v[i]
            P_menor = i

print(v)
print(f"O maior valor é {maior} e está na posição [{P_maior}]")
print(f"O menor valor é {menor} e está na posição [{P_menor}]")