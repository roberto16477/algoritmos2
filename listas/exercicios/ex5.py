a = []
b = []
c = []
n = 5
mult = 0
aux = 0

item = 0

for i in range(n):
    print(f"Informe o {i+1}º valor da primeira lista")
    item = int(input("Informe o valor: "))
    a.append(item)

    print(f"Informe o {i+1}º valor da segunda lista")
    item = int(input("Informe o valor: "))
    b.append(item)

for i in range(n):
    c.append(a[i])

for i in range(n):
    c.append(b[i])

print(a)
print(b)
print(c)
