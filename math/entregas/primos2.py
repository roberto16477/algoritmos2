INICIO = 2
FINAL = 100
V = []
primo = False

for j in range (INICIO, FINAL):
    mult = 0
    for i in range(2, j):
        if j % i == 0:
            mult +=1
            break
    if mult == 0:
        V.append(j)

numero = int(input("Informe um número para verificar se é primo: "))

for k in V:
    if numero % k == 0:
        print("O número ", numero, "não é um número primo!")
        primo = False
        break
    else:
        primo = True

if primo == True:
    print("O número ", numero, "è um número primo!")


#print("Os primos entre ", INICIO, " e ", FINAL, "são:")
#print(V)