n = 5
V1 = []
V2 = []

for i in range(n):
    V1.append(float(input("Informe um valor para o primeiro vetor: ")))

for j in range(n):
    if V1[j] != 0:
        V2.append(V1[j])

if len(V2) == 0:
    print("O vetor é vazio pois o vetor inicial continha apenas zeros")
else:
    print(V2)