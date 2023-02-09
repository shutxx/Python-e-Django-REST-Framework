import requests

headers = {'Authorization': 'Token ec38d3d354eba9a943a61dcd060469f6c979e301'}
url_base_curso = 'http://localhost:8000/api/v2/Cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/Avaliacoes/'

resultado = requests.delete(url=f'{url_base_curso}6/', headers=headers)

assert resultado.status_code == 204  # Testando o código HTTP delete

assert len(resultado.text) == 0  # Testando se o tamanho do conteúdo retorno e 0