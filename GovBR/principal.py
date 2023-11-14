from funcoes import *

opcao = 30
cont = 0
repetir = 0

while opcao != 0:
    if cont >= 1:
        repetir = int(input("Deseja repetir a operação? (informe 1 para SIM ou 2 para NÃO)"))
        
    if repetir != 1:
        print("Informe 0 para sair")
        print("Informe 3 para procurar por domínios relacionados a uma palavra específica")
        print("Informe 5 para consultar a disponibilidade de um domínio")
        opcao = int(input("Informe o número da operação que deseja: "))

    if opcao == 3:
        busca = input("Informe uma palavra para verificar seus domínios: ")

        AgrupaPorPalavra(busca)

    if opcao == 5:
        busca = input("Informe um domínio que deseja consultar do .gov.br")

        ConsultaDominio(busca)

    cont += 1

print("Fim da execução")
