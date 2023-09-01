import numpy as np

n = 5
vetor = np.zeros(n)

for i in range(n):
    vetor[i] = int(input("Informe um valor: "))

soma = vetor.sum()

maior = vetor.max()
menor = vetor.min()
media = vetor.mean()

print("A soma dos valores do vetor é: ", soma)
print("O maior valor do vetor é: ", maior)
print("O menor valor do vetor é: ", menor)
print("A média dos valores do vetor é: ", media) #uso de funções do numpy
