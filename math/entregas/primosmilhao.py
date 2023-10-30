INICIO = 2
FINAL = 100
V = []
primo = False
primosmilhao = []
cont = 0

for j in range (INICIO, FINAL+1):
    mult = 0
    for i in range(2, j):
        if j % i == 0:
            mult +=1
            break
    if mult == 0:
        V.append(j)

inicio2 = 100
final2 = 10000

for k in range(inicio2, final2+1):
    primo = False
    for l in V:
        if k % l == 0:
            primo = False
            break
        else:
            primo = True
    if primo == True:
        primosmilhao.append(k)
        cont += 1
    

print("Os primos de 0 a 100 são: ", V)
print("Os primos no intervalo informado são:", primosmilhao)
print("Existem", cont, "números primos entre 100 e 10.000")
