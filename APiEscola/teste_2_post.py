import requests

headers = {'Authorization': 'Token ec38d3d354eba9a943a61dcd060469f6c979e301'}
url_base_curso = 'http://localhost:8000/api/v2/Cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/Avaliacoes/'

novo_curso = {
    "titulo": "gerência ágil de projetos",
    "url": "http://www.geekuniversity.com.br/scrum"
}

resultado = requests.post(url=url_base_curso, headers=headers, data=novo_curso)

assert resultado.status_code == 201  # Testando o código de status HTTP 201 'CREATE'
assert resultado.json()['titulo'] == novo_curso['titulo']  # Testando se o titulo do curso retornado e o mesmo do informado