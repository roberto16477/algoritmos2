qualquer = int(input("Informe o número de parada: "))
Divisores = []
V = []
primo = False

raiz = qualquer**0.5

RaizInteira = int(raiz)

for j in range (2, RaizInteira+1):
    mult = 0
    for i in range(3, j):
        if j % i == 0:
            mult +=1
            break
    if mult == 0:
        V.append(j)

for l in V:
    if qualquer % l == 0:
        Divisores.append(l)
        primo = False
    else:
        primo = True
        break

if primo == False:
    print("O número", qualquer, "não é primo pois é divisivel por:")
    print(Divisores)
else:
    print("O número", qualquer, "é um número primo!")
