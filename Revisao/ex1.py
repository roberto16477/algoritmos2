n = 5
V1 = []
V2 = []

V3 = []
produtoescalar = 0

for i in range(n):
    V1.append(float(input("Informe um valor para o primeiro vetor: ")))

for j in range(n):
    V2.append(float(input("Informe um número para o segundo vetor: ")))

for k in range(n):
    V3.append(V1[k]*V2[k])

produtoescalar = sum(V3)

print("O vetor 1 é: ", V1)
print("O vetor 2 é: ",V2)
print("O produto escalar é: ", produtoescalar)
