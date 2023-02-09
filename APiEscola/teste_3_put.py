import requests

headers = {'Authorization': 'Token ec38d3d354eba9a943a61dcd060469f6c979e301'}
url_base_curso = 'http://localhost:8000/api/v2/Cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/Avaliacoes/'

curso_atualizado = {
    "titulo": "novo curso de scrum 3",
    "url": "http://www.geekuniversity.com.br/ncs3"
}
resultado = requests.put(url=f'{url_base_curso}6/', headers=headers, data=curso_atualizado)  # http://localhost:8000/api/v2/Cursos/6/

assert resultado.status_code == 200  # Testando o código de status HTTP 201 'CREATE'
assert resultado.json()['titulo'] == curso_atualizado['titulo']  # Testando se o titulo do curso retornado e o mesmo do informado

curso = requests.get(url=f'{url_base_curso}6/', headers=headers)  # http://localhost:8000/api/v2/Cursos/6/
print(curso.json())