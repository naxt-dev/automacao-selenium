import unittest
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.login_page import LoginPage

class TestLogin(unittest.TestCase):

    def setUp(self):
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        
        self.driver = webdriver.Edge(
            service=Service(EdgeChromiumDriverManager().install()),
            options=options
        )
        self.login_page = LoginPage(self.driver)
        self.login_page.open()
        time.sleep(1)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_login_sucesso(self):
        self.login_page.login("tomsmith", "SuperSecretPassword!")
        mensagem = self.login_page.get_flash_message()
        self.assertIn("You logged into a secure area!", mensagem)

    def test_login_senha_invalida(self):
        self.login_page.login("tomsmith", "senha_incorreta_123")
        mensagem = self.login_page.get_flash_message()
        self.assertIn("Your password is invalid!", mensagem)

    def test_login_usuario_invalido(self):
        self.login_page.login("usuario_fantasma", "SuperSecretPassword!")
        mensagem = self.login_page.get_flash_message()
        self.assertIn("Your username is invalid!", mensagem)

if __name__ == "__main__":
    unittest.main()