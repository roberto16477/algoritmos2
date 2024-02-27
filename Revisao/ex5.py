M = []
N = 10

for i in range(N):
    lista = []
    for j in range(N):
        if i == j:
            lista.append(3*(i**2))
        elif i < j:
            lista.append((2*i)+(7*j))
        else:
            lista.append((4*i**3)+(5*j**2)+(1))
    M.append(lista)

for x in M:
    print(x)