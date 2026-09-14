from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        """Espera até que o elemento esteja visível na tela e o retorna."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Espera o elemento ficar clicável e executa o clique."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        """Limpa o campo de texto e digita a string informada."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Retorna o texto contido no elemento visível."""
        return self.find(locator).text