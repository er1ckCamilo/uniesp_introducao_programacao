# Alunos: Erick, Bonifácio, Edivan JR, Sergio Japa
# Turma: SI/SPI P1B
# Projeto de avaliação Unidade 2

from requests import get
from json import dumps
from os import system
from sys import stderr

LIMPAR_TELA = 'cls' # Comando para limpar tela: Windows -> cls | Linux -> clear
BANCO_DADOS = 'database.txt'
SEPARADOR = '|'
LIMITE_CIDADE_LINHA = 3
LANG = 'pt_br'

def banner():
    system(LIMPAR_TELA)
    print('\t\t**********************************')
    print('\t\t******   OPEN WEATHER       ******')
    print('\t\t******   Turma: P1B         ******')
    print('\t\t******   Aluno: Erick       ******')
    print('\t\t******   Aluno: Bonifácio   ******')
    print('\t\t******   Aluno: Edivan JR   ******')
    print('\t\t******   Aluno: Sergio Japa ******')
    print('\t\t**********************************\n')

def menu():
    banner()
    print('\t\t  Escolha uma das opções abaixo:\n\n')
    print('\t(1) Cadastrar uma Cidade   (2) Listar cidades cadastradas')
    print('\t(3) Obter as informações de uma cidade   (4) Obter as informações de todas as cidades')
    print('\t(5) Sair do programa\n')
    
    escolha = int(input('[>] Informe o número da opção escolhida: '))
    return escolha

def dado_vazio(dado):
    if dado == None or dado == '' or (type(dado) == list and len(dado) == 0) or (type(dado) == list and (len(dado) == 1 and dado[0] == '')):
        return True
    else:
        return False

def pausar():
    input('Pressione qualquer tecla para continuar...')

def cadastrar_cidade(info):
    try:
        with open(BANCO_DADOS, 'a', encoding='UTF-8') as b_dados:
            b_dados.write(info + '\n')
        print('[+] Cidade cadastrada com sucesso !')
    except Exception as msg_err:
        print(f'[INFO] Ocorreu um erro: {msg_err}',file=stderr)

def ler_banco_dados():
    try:
        with open(BANCO_DADOS, 'r',encoding='UTF-8') as b_dados:
            dados = []
            for linha in b_dados.readlines():
                linha = linha.replace('\n','').split(SEPARADOR)
                dados.append(linha)
        return dados
    except FileNotFoundError:
        print(f'[INFO] Base de dados não encontrada, cadastre uma cidade ou crie o arquivo {BANCO_DADOS} no mesmo diretorio.',file=stderr)

def consultar_api(chave,latitude,longitude):
    url = (f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={chave}&lang={LANG}')
    responsta = get(url)
    return responsta.json()

def exportar_dados_cidade(nome_cidade,dados):
    try:
        nome_arquivo = nome_cidade + '.json'
        with open(nome_arquivo, 'w',encoding='UTF-8') as arquivo:
            dados_json = dumps(dados, indent=4)
            arquivo.write(dados_json)
    except Exception as msg_err:
        print(f'[INFO] Ocorreu um erro: {msg_err}',file=stderr)

while True:
    op = menu()
    
    if op <= 0 or op > 5:
        print(f'[INFO] Opção inválida: {op}', file=stderr)
        break
    elif op == 1:
        banner()
        print(f'\t\t  Cadastro de cidades\n')
        nome_cidade = input('[>] Digite o nome da cidade: ')
        lat = input('[>] Informe a latitude: ')
        lon = input('[>] Infomre a longitude: ')
        dados = SEPARADOR.join([nome_cidade,lat,lon])
        cadastrar_cidade(dados)
        pausar()
    elif op == 2:
        banner()
        print(f'\t\t  Listando cidades...\n')
        dados = ler_banco_dados()
        contador = 1
        if not dado_vazio(dados):
            for info in dados:
                print(f'{contador} - {info[0]} | latitude: {info[1]} | longitude: {info[2]}')
                contador += 1
        else:
            print('[INFO] Nenhuma cidade cadastrada')
        pausar()
    elif op == 3:
        banner()
        print(f'\t\t  Consultar informações da cidade na API\n')
        dados = ler_banco_dados()
        contador = 1
        linha = 0
        if not dado_vazio(dados):
            for info in dados:
                if linha == LIMITE_CIDADE_LINHA:
                    print(' ')
                    linha = 0
                print(f'({contador}) - {info[0]}',end='  ')
                contador += 1
                linha += 1

            cidade_id = int(input('\n\n[>] Digite o número da cidade que deseja: '))
            key = input('[>] Informe a sua chave para consultar a API: ')
            if cidade_id <= 0 or cidade_id > len(dados):
                print(f'[INFO] Opção inválida: {cidade_id}')
            else:
                banner()
                print('\t\t  Obtendo informações da cidade...\n')
                lat = dados[cidade_id - 1][1]
                lon = dados[cidade_id - 1][2]
                cidade = dados[cidade_id - 1][0]

                dados_cidade = consultar_api(key,lat,lon)
                exportar_dados_cidade(cidade,dados_cidade)
                print(f'[+] O arquivo com as informações da cidade foi criado: {cidade}.json')
        else:
            print('[INFO] Nenhuma cidade cadastrada')
        pausar()
    elif op == 4:
        banner()
        print('\t\t Consultando todas as cidades cadastradas...\n')
        key = input('[>] Informe a sua chave para consultar a API: ')
        dados = ler_banco_dados()
        if not dado_vazio(dados):
            for info in dados:
                cidade = info[0]
                lat = info[1]
                lon = info[2]
                dados_json = consultar_api(key,lat,lon)
                exportar_dados_cidade(cidade,dados_json)
                print(f'[+] Arquivo com as informações de {cidade} criado: {cidade}.json')
        else:
            print('[INFO] Nenhuma cidade cadastrada')
        pausar()
    else:
        break


