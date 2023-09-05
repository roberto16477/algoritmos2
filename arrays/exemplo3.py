a = [1]
i = 0

while a[i] != 0:
    n = (int(input("Digite um numero: ")))
    if n == 0:
        break
    else:
        a.append(n)
    i = i+1


print(a)