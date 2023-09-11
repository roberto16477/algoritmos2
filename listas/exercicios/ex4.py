l1 = []
l2 = []
l3 = []
n = 5
mult = 0
aux = 0

item = 0

for i in range(n):
    print(f"Informe o {i+1}º valor da primeira lista")
    item = int(input("Informe o valor: "))
    l1.append(item)

    print(f"Informe o {i+1}º valor da segunda lista")
    item = int(input("Informe o valor: "))
    l2.append(item)

for i in range(n):
    aux = n - (i + 1)
    mult = l1[i] * l2[aux]
    l3.append(mult)

print("Lista 1: ", l1)
print("Lista 2: ", l2)
print("Lista 3: ", l3)
