v1 = []
v2 = []
v3 = []
n = 10

for i in range(n):
    v1.append(int(input(f"Informe o {i+1}º número do primeiro vetor: ")))

for j in range(n):
    v2.append(int(input(f"Informe o {j+1}º número do segundo vetor: ")))

for k in range(n):
    v3.append(v1[k])
    v3.append(v2[k])

print("O terceiro vetor é: ", v3)
