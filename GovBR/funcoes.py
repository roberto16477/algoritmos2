def ContaLinhas(nome):
    with open(f"GovBR/{nome}", "r", encoding="utf-8") as dominios:
        contagem = dominios.readlines()
        cont = 0

        for linha in contagem:
            cont += 1
        
        print(f"\nO arquivo {nome} possui {cont} linhas")
        print("Com as colunas:")
        print(Colunas())



def AnoCadastro():
    with open("GovBR/dominios.csv", "r", encoding="utf-8") as dominios:
        todos = dominios.readlines()
        nomearq = input("\nInforme o nome que o arquivo deverá ter: ")
        anobusca = input("Informe o ano para ver todos os domínios .gov.br criados no ano informado")

        with open(f"GovBR/{nomearq}.txt", "w", encoding="utf-8") as allyear:
            for linha in todos:
                colunas = linha.split('|')
                if anobusca in colunas[7]:
                    allyear.write(linha)
            print(f"foi criado o arquivo{nomearq}.txt com todos os domínios cadastrados no ano de {anobusca}")
    
    resposta = 0
    while (resposta > 2) or (resposta < 1):
        print("\nDeseja obter mais informações sobre o arquivo?")
        resposta = int(input("digite 1 para SIM ou 2 para NÃO"))

    if resposta == 1:
        ContaLinhas(f"{nomearq}.txt")

            
        

def Colunas():
    with open("GovBR/dominios.csv", "r", encoding="utf-8") as dominios:
        cabecalho = dominios.readline()
        return(cabecalho)



def AgrupaPorPalavra(palavra):
    with open("GovBR/dominios.csv","r", encoding="utf-8") as dominios:
        todos = dominios.readlines()
        existe = 0

    informacao = palavra.lower()

    for linha in todos:
        colunas = linha.split('|')
        if informacao in linha:
            print(colunas[1])
            existe += 1
        
    if existe < 1:
        print("Não existem domínios com a palavra: ", palavra)



def estatisticas(anoinicio, anofim):
    with open("GovBR/dominios.csv","r", encoding="utf-8") as dominios:
        todos = dominios.readlines()
        anosv = []
        maiorreg = 0
        menorreg = 0

        for ano in range(anoinicio, anofim + 1):
            anostr = str(ano)
            for linha in todos:
                colunas = linha.split('|')

                if anostr in colunas[7]:
                    anosv.append(ano)
        
        soma = 0

        for ano2 in range(anoinicio, anofim +1):
            segundo = anosv.count(ano2)
            soma = soma + segundo
            divisor = (anofim - anoinicio) + 1
        
        d = {i: anosv.count(i) for i in set(anosv)}
        maiorreg = max(d, key=d.get)
        menorreg = min(d, key=d.get)
        media = (soma / divisor)

    print("A média de cadastros por ano é: ", media)
    print("O ano com mais cadastros é: ", maiorreg)
    print("O ano com menos cadastros é: ", menorreg)



def ConsultaDominio(dominio):
    with open("GovBR/dominios.csv","r", encoding="utf-8") as dominios:
        todos = dominios.readlines()

        busca = (dominio.lower() + ".gov.br")
        existe = 0

        for linha in todos:
            if busca in linha:
                print(f"\nO domínio {busca} já existe!")
                print(linha)
                existe += 1
        
        if existe < 1:
            print(f"O domínio {busca} está livre!")

           
def RegistrosHandle():
    regh = []
    with open("GovBR/dominios.csv", "r", encoding="utf-8") as dominios:
        todos = dominios.readlines()

        with open("GovBR/opcoes_handle.txt", "w", encoding="utf-8") as opcoeshandle:
            for linha in todos:
                colunas = linha.split('|')

                if colunas[3] not in regh:
                    regh.append(colunas[3])
                    opcoeshandle.write(f"{colunas[3]}\n")

                if colunas[4] not in regh:
                    regh.append(colunas[4])
                    opcoeshandle.write(f"{colunas[4]}\n")

                if colunas[5] not in regh:
                    regh.append(colunas[5])
                    opcoeshandle.write(f"{colunas[5]}\n")

        print("Foi gerado o arquivo opcoes_handle.txt com todas as opções usadas nas colunas Handle")



