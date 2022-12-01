import unittest

from selenium.webdriver.chrome.webdriver import WebDriver


class TestWebDriver(unittest.TestCase):
    def setup(self) -> None:
        self.url: str = "https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx"
        self.web_driver: WebDriver = WebDriver()
        self.web_driver.get(self.url)

    def test_retorno_200_do_site(self) -> None:
        self.assertEqual(self.web_driver)
