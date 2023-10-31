arquivo = open("Aula_arquivos/nome.txt", "w")

nome = input("Informe o nome a ser escrito: ")

arquivo.write(f"{nome}")

print(nome)

arquivo.close()