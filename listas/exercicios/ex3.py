l1 = []
l2 = []
l3 = []
n = 5
soma = 0

item = 0

for i in range(n):
    print(f"Informe o {i+1}º valor da primeira lista")
    item = int(input("Informe o valor: "))
    l1.append(item)

    print(f"Informe o {i+1}º valor da segunda lista")
    item = int(input("Informe o valor: "))
    l2.append(item)

for i in range(n):
    soma = l1[i] + l2[i]
    l3.append(soma)

print("Lista 1: ", l1)
print("Lista 2: ", l2)
print("Lista 3: ", l3)
