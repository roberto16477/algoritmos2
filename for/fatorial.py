print ("Calculo de fatorial:")

n = int(input("Informe um número inteiro positivo: "))
fat = 1

for i in range(1, n+1):
    fat = fat*i
    print(fat)

print(f"{n} ! = {fat}")
