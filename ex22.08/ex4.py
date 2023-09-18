resultado = []
aposta = []
cont = 0
nresultado = 5
naposta = 10
nx = 0

for i in range(nresultado):
    resultado.append(int(input(f"informe o {i+1}º número do resultado: ")))

for i in range(naposta):
    aposta.append(int(input(f"Informe o {i+1}º numero da aposta: ")))

for i in range(nresultado):
    nx = resultado[i]
    for j in range(naposta):
        if aposta[j] == nx:
            cont+=1

print("A aposta foi: ", aposta)
print("O resultado foi: ", resultado)
print(f"A aposta fez {cont} pontos")
