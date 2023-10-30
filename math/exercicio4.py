INICIO = int(input("Informe o primeiro número do intervalo: "))
FINAL = int(input("Informe o último número do intervalo: "))
V = []


for j in range (INICIO, FINAL+1):
    raiz = j**0.5
    if (raiz * 2) % 2 == 0:
        V.append(j)

print("Os números com quadrados perfeitos são:")
print(V)
