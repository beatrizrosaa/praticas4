import unittest
from app.app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_print_health_check(self):
        response = self.app.get('/health-check')
        self.assertEqual(200, response.status_code, "Erro no test_http_code!")
        self.assertEqual("<h1>Hello, I'm Alive!</h1>", response.get_data(as_text=True)
                          , "Erro no test_print_health_check!")

    def test_hello_no_name(self):
        # Testa a rota /hello sem passar o parâmetro 'name' (deve retornar 400)
        response = self.app.get('/hello')
        self.assertEqual(400, response.status_code)
        self.assertEqual("Nome não informado", response.get_data(as_text=True))

    def test_hello_with_name(self):
        # Testa a rota /hello passando o parâmetro 'name'
        response = self.app.get('/hello?name=Beatriz')
        self.assertEqual(200, response.status_code)
        self.assertEqual("Hello, Beatriz!", response.get_data(as_text=True))