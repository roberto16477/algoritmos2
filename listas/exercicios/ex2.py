x = []
n = 10

for i in range(n):
    item = int(input("Informe um valor para adicionar a lista X: "))
    x.append(item)

for i in range(n):
    if x[i] % 2 == 0:
        x[i] = x[i]*i
    else:
        x[i] = i

print(x)
