#gerando arquivos com resultados que obtiver com o código
with open ("manipulacao-arquivos/textos/impares.txt", "w") as impares:
    with open("manipulacao-arquivos/textos/pares.txt", "w") as pares:
        for i in range(0, 1000):
            if i % 2 == 0:
                pares.write(f"{i}\n")
            else:
                impares.write(f"{i}\n")
