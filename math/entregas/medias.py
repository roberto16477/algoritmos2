A = float(input("Informe um valor para A: "))
B = float(input("Informe um valor para B: "))
MH = 0
MA = 0
MG = 0
cont = 0
diferenca = 1
parada = 10**-2

while diferenca > parada:
    MH = (2*A*B) / (A+B)
    MA = (A+B)/2
    A = MH
    B = MA
    MG = ((A*B)**0.5)
    cont += 1
    diferenca = MA - MH

print("Quantidade de interações realizadas: ", cont)
print("A média harmonica é: ", MH)
print("A média geométrica é: ", MG)
print("A média aritmética é: ", MA)
