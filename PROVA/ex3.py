X = []
N = 100
cont = 0
contimp = 0
soma = 0
media = 0

for i in range(N):
    X.append(int(input("Informe um valor: ")))

for j in range(N):
    if X[j] % 2 == 0:
        cont = cont + 1
    else:
        soma = soma + X[j]
        contimp += 1
    media = soma/contimp


print("O total de numeros pares em X é: ", cont)
print("A média dos valorem impares em X é: ", media)
