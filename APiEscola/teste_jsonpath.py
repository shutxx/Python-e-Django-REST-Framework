import requests
import jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/Avaliacoes/')  # Acessando endpoint GET Avaliacoes
resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')  # Acessando todos os resultados
primeiro = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')  # Acessando apenas primeiro resultado
nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')  # Acessando o nome do primeiro resultado
nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')  # Acessando todos os nomes de todos os resultados
print(resultados)
print(primeiro)
print(nome)
print(nomes)

"""
avaliacoes = requests.get('http://localhost:8000/api/v2/Avaliacoes/')
id = jsonpath.jsonpath(avaliacoes.json(), 'results[0].id')
curso = jsonpath.jsonpath(avaliacoes.json(), 'results[0].curso')
nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
comentario = jsonpath.jsonpath(avaliacoes.json(), 'results[0].comentario')
avaliacao = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
criacao = jsonpath.jsonpath(avaliacoes.json(), 'results[0].criacao')
ativo = jsonpath.jsonpath(avaliacoes.json(), 'results[0].ativo')
print(f'id:{id} curso:{curso} nome:{nome} comentario:{comentario} avaliacao:{avaliacao} criacao:{criacao} ativo:{ativo}')
"""