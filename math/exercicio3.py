INICIO = int(input("Informe o primeiro número do intervalo: "))
FINAL = int(input("Informe o último número do intervalo: "))
V = []


for j in range (INICIO, FINAL):
    mult = 0
    for i in range(2, j):
        if j % i == 0:
            mult +=1
            break
    if mult == 0:
        V.append(j)

print("Os primos entre ", INICIO, " e ", FINAL, "são:")
print(V)
