#
from funcoes import *

opcao = 30
cont = 0
repetir = 2

while opcao != 0:
    if (cont >= 1) and (opcao != 29):
        repetir = int(input("\nDeseja repetir a operação? (informe 1 para SIM ou 2 para NÃO)"))
        
    if repetir == 2:
        print("\nInforme 0 para sair")
        print("Informe 1 para verificar o número de registros do arquivo dominios.csv e quais suas colunas")
        print("Informe 2 para verificar todos os cadastros de um ano específico")
        print("Informe 3 para procurar por domínios relacionados a uma palavra específica")
        print("Informe 4 para ver as estatísticas de um período específico")
        print("Informe 5 para consultar a disponibilidade de um domínio")
        print("Informe 6 para gerar um arquivo txt com as opções já cadastradas nas colunas handle")
        opcao = int(input("Informe o número da operação que deseja: "))
    
    if (opcao > 6) or (opcao < 0):
        opcao = 29
        print("\n******************   Operação inválida!   ******************")

    if opcao == 1:
        ContaLinhas("dominios.csv")
    elif opcao == 2:
        AnoCadastro()

    if opcao == 4:
        parametroinicio = int(input("\nInforme o ano inicial da consulta: "))
        parametrofim = int(input("Informe o ano final da consulta: "))
        estatisticas(parametroinicio, parametrofim)

    if opcao == 3:
        busca = input("\nInforme uma palavra para verificar seus domínios: ")

        AgrupaPorPalavra(busca)

    if opcao == 5:
        busca = input("\nInforme um domínio que deseja consultar do .gov.br: ")

        ConsultaDominio(busca)

    if opcao == 6:
        RegistrosHandle()
        
    cont += 1

print("\nFim da execução")
