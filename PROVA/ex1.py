V = []
R1 = []
R2 = []
N = 8

for i in range(N):
    V.append(int(input("Informe um valor: ")))

for j in range(N):
    if V[j] > 0:
        R1.append(V[j])
    elif V[j] < 0:
        R2.append(V[j])

print("Vetor Original: ", V)
print("Resultante 1: ", R1)
print("Resultante 2: ", R2)
