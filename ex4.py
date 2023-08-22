x = []

for i in range (0, 10):
    x.append(int(input("Numero: ")))

for i in range(10):
    if (x[i] % 2 == 0):
        x[i] = x[i]*i
    else:
        x[i] = i

print(x) 