from selenium import webdriver
import unittest


class TestNovoUsuario(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_adicionar_um_novo_item_de_compra(self):
        self.browser.get('http://localhost:5000')

        # Na aba de titulos ele vê a palavra Metas
        self.assertIn('Metas', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
