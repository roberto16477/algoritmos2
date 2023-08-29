n = 9
v = []
v2 = []

for num in range(9):
    valor = int(input("Digite um número: "))
    v.append(valor)

for i in range(n):
    mult = 0
    for j in range (2,v[i]-1):
        if v[i] % j == 0:
            mult += 1
    if mult == 0:
        v2.append(i)

print(v2)