n = 10
v = []
num = 0

for i in range(n):
    num = int(input("Informe um número: "))
    if num not in v:
        v.append(num)

print(v)