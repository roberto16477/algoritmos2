N = int(input("Informe um numero: "))
V = []

for i in range(1, N+1):
    if N % i == 0:
        V.append(i)

print(N, "É divisivel por: ", V)
