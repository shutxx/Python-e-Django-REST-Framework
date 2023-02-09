import requests

#  Request basicos
avaliacoes = requests.get('http://localhost:8000/api/v2/Avaliacoes/')  # Acessando endpoint GET Avaliacoes
print(avaliacoes.status_code)  # Acessando o código de status HTTP
print(avaliacoes.json())  # Acessando os dados da resposta
print(type(avaliacoes.json()))  # Acessando 'type/tipo' da resposta
print(avaliacoes.json()['count'])  # Acessando a quantidade de registros
print(avaliacoes.json()['next'])  # Acessando a proxima página de resultados
print(avaliacoes.json()['results'])  # Acessando os resultados desta página
print(type(avaliacoes.json()['results']))  # Acessando 'type/tipo' da resposta
print(avaliacoes.json()['results'][0])  # Acessando elementos da lista
print(avaliacoes.json()['results'][-1]['nome'])  # Acessando o nome do último elemento

# Request em endpoint especifico
avaliacao = requests.get('http://localhost:8000/api/v2/Avaliacoes/5/')  # Acessando endpoint de uma avaliacao especifica
print(avaliacao.json())

# Request com cabeçalho
headers = {'Authorization': 'Token ec38d3d354eba9a943a61dcd060469f6c979e301'}
cursos = requests.get(url='http://localhost:8000/api/v2/Cursos/', headers=headers)
print(cursos.status_code)
print(cursos.json())