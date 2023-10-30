N = int(input("Informe um número: "))
V = []
mult = 0

for j in range (2, N):
    if N % j == 0:
        mult += 1
        V.append(j)

if mult == 0:
    print(N, "é um número primo!")
else:
    print(N, "é divisivel por: ", V)
