import json
from re import I
import requests

# URL do WebService
url = "http://177.101.203.139/edecio/filmes.json"


def titulo(msg, traco="-", tam=50):
    print()
    print(msg)
    print(traco*tam)


def listar_filmes():
    titulo(msg="Listagem de Filmes do Servidos ", tam=98)
    response=requests.get(url)
    filmes=json.loads(response.text)
    


    print("ID. Titulo do Filme...................: Genero..............: Distribuidora...........: Ano de Exibição.:  Publico de exibição no Ano..:")
    # retorna os dados da url
    for filme in filmes:
        print(
            f"{filme['id']:4d} {filme['titulo'][0:35]:35s} {filme['genero'][0:25]:25s}{filme['empresa_distribuidora'][0:25]:25s}{filme['ano_exibicao']:10d}{filme['publico_ano_exibicao']:15d}")





#2
def filtrar_paises():
    titulo(msg="Filtrar por Países cadastrados", tam=98)

    response=requests.get(url)
    filmes=json.loads(response.text)

    pais = input("Informe o País: ")


    print("ID. Titulo do Filme...................: Publico........: País Produtor da Obra...........:")

    contador = 0

    for filme in filmes:
        if filme['pais_produtor_obra'] == pais:
            print(
                f"{filme['id']:4d} {filme['titulo'][0:35]:35s} {filme['publico_ano_exibicao']:16d} {filme['pais_produtor_obra'][0:33]:33s}")
            contador += 1                

    if contador == 0:
        print("* Obs.: Não há filmes com esse País")








#3
def salvar():
    titulo("Salvar Dados na Máquina Local")

    min_publico = 100000

    response = requests.get(url)
    filmes = json.loads(response.text)    
   
    
    print("Aguarde...")

    dados = []

    for filme in filmes:
        if filme['publico_ano_exibicao'] >= min_publico:
            novo = {"id": filme['id'], "Titulo": filme['titulo'], "Genero": filme['genero'][0:25], "Distribuidora": filme['empresa_distribuidora'][0:25], "Ano de exibicao": filme['ano_exibicao'], "Publico de exibicao no Ano": filme['publico_ano_exibicao']}
            print(f"Salvando: {filme['titulo']}")
            dados.append(novo)

    # salva a lista de dicionários no arquivo dados.json        
        with open("dados.json", "w") as arq:
            json.dump(dados, arq,indent=4)


#4
def listar_local():
    titulo(msg="Listagem de Filmes (máquina local)", tam=98)

    # lê os dados do arquivo e atribui para a variável dados
    with open("dados.json", "r") as arq:
        dados = json.load(arq)

    print("ID. Titulo do Filme...................: Genero..............: Distribuidora...........: Ano de Exibição.:  Publico de exibição no Ano:..")

    for filme in dados:
        print(
            f"{filme['id']:4d} {filme['Titulo'][0:35]:35s} {filme['Genero'][0:25]:25s}{filme['Distribuidora'][0:25]:25s}{filme['Ano de exibicao']:10d}{filme['Publico de exibicao no Ano']:29d}")

#5
def estatisticas():
    titulo("Estatísticas dos Filmes")

    response = requests.get(url)
    filmes = json.loads(response.text)  
    ano = 0
    ano1 = 0
    contador = 0
    soma = len(filmes)

    for i, filme in enumerate(filmes):
        if filme['ano_exibicao'] == 2018:
            ano+=1
        if filme['ano_exibicao']== 2019:
            ano1+=1
        if filme['publico_ano_exibicao'] > 0:
            contador += filme['publico_ano_exibicao']
    
    media = contador/soma

    print(f"Nº de Filmes Cadastrados..: {soma}")
    print(f"Nº de Filmes Exibidos em 2018..: {ano}")
    print(f"Nº de Filmes Exibidos em 2019..: {ano1}")
    print(f"Publico Médio..: {media}")

#6
def agrupar():
    titulo("Nº de Filmes por Gêneros")
    
    response = requests.get(url)
    filmes = json.loads(response.text)
    
    
    # dicionário para receber os tipos de filmes
    tipos = {}
    # tipos{"batom": 1, "pincel": 1}

    for filme in filmes:
        if filme['genero'] in tipos:
            tipos[filme['genero']] += 1
        else:    
            tipos[filme['genero']] = 1

    for tipo in tipos.items():

        print(f"{tipo[0]}: {tipo[1]}")

#7
def filmes_brasileiros():
    titulo("Atualizando Novo Arquivo com Filmes Brasileiros")

    brasileiros = 'Brasil'

    response = requests.get(url)
    filmes = json.loads(response.text)    
   
    
    print("Aguarde...")

    Filmes_Brasileiros = []

    for filme in filmes:
        if filme['pais_produtor_obra'] == brasileiros:
            novo = {"id": filme['id'], "Titulo": filme['titulo'], "Genero": filme['genero'][0:25], "Distribuidora": filme['empresa_distribuidora'][0:25], "Ano de exibicao": filme['ano_exibicao'], "Publico de exibicao no Ano": filme['publico_ano_exibicao'],"pais_produtor_obra":filme['pais_produtor_obra'],"nacionalidade":filme['nacionalidade'],"renda_ano_exibicao":filme['renda_ano_exibicao']}
            
            print(f"Salvando: {filme['titulo']}")
            Filmes_Brasileiros.append(novo)

    # salva a lista de dicionários no arquivo dados.json        
        with open("Filmes_Brasileiros.json", "w") as arq:
            json.dump(Filmes_Brasileiros, arq,indent=4)



#INICIO DO PROGRAMA
while True:
    titulo("Controle de Filmes", "=")
    print("1. Listar Filmes do Servidor")
    print("2. Filtrar por País Produtor do Filme")
    print("3. Salvar dados local(Filmes c/ Publico + 100.000 Pessoas) ")
    print("4. Listar dados do arquivo Local")
    print("5. Estatísticas")
    print("6. Agrupar por gênero")
    print("7. Filmes Brasileiros")
    print("8. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        listar_filmes()
    elif opcao == 2:
        filtrar_paises()
    elif opcao == 3:
        salvar()
    elif opcao ==4:
        listar_local()
    elif opcao ==5:
        estatisticas()
    elif opcao ==6:
        agrupar()
    elif opcao ==7:
        filmes_brasileiros()
    else:
        break
