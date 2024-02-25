n = 10
v = []
num = 0

for i in range(n):
    num = int(input("Informe um número: "))
    while num in v:
        num = int(input(f"O número {num} já existe no vetor. Informe outro número: "))

    v.append(num)

print(v)