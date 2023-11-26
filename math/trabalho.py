numinicial = int(input("Informe o inicio do intervalo: "))
numfinal = int(input("Informe o final do intervalo: "))
primosintervalo = []
V = []
primo = False
cont = 0

raiz = numfinal**0.5

RaizInteira = int(raiz)

for j in range (2, RaizInteira+1):
    mult = 0
    for i in range(2, j):
        if j % i == 0:
            mult +=1
            break
    if mult == 0:
        V.append(j)


for k in range(numinicial, numfinal+1):
    primo = False
    for l in V:
        if k % l == 0:
            primo = False
            break
        else:
            primo = True
    if primo == True:
        primosintervalo.append(k)
        cont += 1
    
print("Os primos no intervalo informado são:", primosintervalo)
print(f"A raiz inteira de {numfinal} é {RaizInteira}")
print("Existem", cont, "números primos no intervalo selecionado!")
