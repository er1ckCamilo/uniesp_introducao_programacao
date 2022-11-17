''' 
    Exemplo Simples da solução da TED usando apenas recursos apresentados em sala.

    Aluno(s): Erick
    Turma: P1B

    - Selecione a Longitude e Latitude das capitais de Portugal, Espanha, Itália, França e Inglaterra;
    - Crie um arquivo TXT organizando as informações: País, Capital, Logintude, Latitude (modelo abaixo);
    - Seu programa deverá utilizar o arquivo como fonte de dados para consumir a API;
    - Utilize uma estrutura de repetição para chamar a API até o final dos dados;
    - Imprima o resultado em arquivos JSON separados, e cada um deverá conter o nome do país específico;
'''

# Digite o seguinte comando no terminal para instalar a biblioteca requests ou json (Se necessario).
# Comando: python -m pip install requests
# Comando: python -m pip install json

# Importando apenas a função que vamos usar
from requests import get 
from json import dumps

API_KEY = input("Digite sua chave para utilizar a API: ")
nome_arquivo = input("Informe o arquivo com os dados que deve ser consultados: ")

# Lendo o arquivo e tratando os dados para facilitar o acesso as informações
dados = []
with open(nome_arquivo , 'r', encoding='UTF-8') as arquivo:
    for linha in arquivo.readlines():
        linha = linha.replace('\n','').replace(' ','') # Remove a quebra de linha e os espaços
        novo_formato = linha.split(',') # Separa os elementos por "," e retorna uma lista
        dados.append(novo_formato) # Colocando os dados formatados em uma lista

# Enviando as requisições para a API
for info in dados:    
    # Formatando a url com latitude, longitude e a chave para consultar a API
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={info[3]}&lon={info[2]}&appid={API_KEY}'   
    resposta = get(url) # Faz a requisição para a API

    # Se a requisição foi aceita com sucesso, cria o arquivo com os dados que foi retornado
    if resposta.status_code == 200:
        print(f'Criando arquivo: {info[0]}.json')
        with open(info[0] + '.json', 'w', encoding='UTF-8') as arquivo:
            dados_json = dumps({info[1]:resposta.json()}, indent=4) # Converte um dicinoario para uma string json
            arquivo.write(dados_json)
    else:
        print(f'Ocorreu um erro ao consultar as informações para: {info}')

