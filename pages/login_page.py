from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # URL de testes pública muito usada para treinar automação
    URL = "https://the-internet.herokuapp.com/login"

    # Mapeamento dos elementos (Locators)
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def open(self):
        """Navega até a página de login."""
        self.driver.get(self.URL)

    def login(self, username, password):
        """Preenche os campos de login e clica em enviar."""
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_flash_message(self):
        """Captura o texto do alerta de sucesso/erro."""
        return self.get_text(self.FLASH_MESSAGE)