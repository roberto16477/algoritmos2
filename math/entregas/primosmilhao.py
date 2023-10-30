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

inicio2 = int(input("Informe o inicio do intervalo: "))
final2 = int(input("Informe o final do intervalo: "))

for k in range(inicio2, final2):
    for l in V:
        if k % l == 0:
            break
        else:
            

