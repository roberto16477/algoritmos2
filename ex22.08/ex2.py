n = 5
v = []
v2 = []
v3 = []

for num in range(n):
    valor = int(input("Digite um número: "))
    v.append(valor)

for i in range(n):
    mult = 0
    for j in range (2,v[i]-1):
        if v[i] % j == 0:
            mult += 1
    if mult == 0:
        v2.append(i)
        v3.append(v[i])

print("as posições são: ", v2)
print("Os valores são: ", v3)