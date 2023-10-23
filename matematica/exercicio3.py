INICIO = int(input("Informe o primeiro número do intervalo: "))
FINAL = int(input("Informe o último número do intervalo: "))
V = []
mult = 0

for j in range (INICIO, FINAL):
    for i in range(2, j):
        if j % i == 0:
            mult += 1
            V.append(j)

if mult == 0:
    print(N, "é um número primo!")
else:
    print(N, "é divisivel por: ", V)