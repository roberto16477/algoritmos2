arqnome = open("pastaa/nome.txt", "w")

nome = input("Informe o nome: ")

arqnome.write(nome)

print("O nome é: ", nome)

arqnome.close()