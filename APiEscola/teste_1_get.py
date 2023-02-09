import requests

headers = {'Authorization': 'Token ec38d3d354eba9a943a61dcd060469f6c979e301'}
url_base_curso = 'http://localhost:8000/api/v2/Cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/Avaliacoes/'

resultado = requests.get(url=url_base_curso, headers=headers)  # Acessando endpoint GET Avaliacoes
print(resultado.json())
print(resultado.status_code)

assert resultado.status_code == 200  # Testando se endpoint está correto

assert resultado.json()['count'] == 6  # Testando a quantidade de registros

assert resultado.json()['results'][0]['titulo'] == 'curso010'  # Testando se o titulo do primeiro curso está correto

