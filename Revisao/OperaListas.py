from funcfilas import *

lista = []
n = int(input("Quantos valores terá a lista? "))
inserir(n, lista)

tirar = input("Informe um valor para ser removido da lista: ")
remover(tirar, lista)



VC = input("Informe o valor que deseja consultar: ") # VC = Valor Consulta
if consulta in lista:
    print(f"O valor {consulta} está na lista!")
else:
    print("TEM NADA AQUI NAO")

print(f"A lista")
