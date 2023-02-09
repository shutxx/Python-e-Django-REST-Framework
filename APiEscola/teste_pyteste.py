import requests
#  pytest teste_pyteste.py


class TestCursos:
    headers = {'Authorization': 'Token ec38d3d354eba9a943a61dcd060469f6c979e301'}
    url_base_curso = 'http://localhost:8000/api/v2/Cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_curso, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_curso}3/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "curso de programacao com ruby",
            "url": "http://www.geekuniversity.com.br/cpr"
        }
        resposta = requests.post(url=self.url_base_curso, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "novo curso de ruby",
            "url": "http://www.geekuniversity.com.br/ncr"
        }

        resposta = requests.put(url=f'{self.url_base_curso}4/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "novo curso de ruby 2",
            "url": "http://www.geekuniversity.com.br/ncr2"
        }
        resposta = requests.put(url=f'{self.url_base_curso}4/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete(self):
        resposta = requests.delete(url=f'{self.url_base_curso}4/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0