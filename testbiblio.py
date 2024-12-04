import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = False 
        service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service, options=options)

    def test_login_successful(self):
        """Prueba de inicio de sesión con credenciales correctas."""
        self.driver.get("http://localhost/biblioteca/")

       
        username_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "usuario"))
        )
        password_box = self.driver.find_element(By.ID, "clave")
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-block")

        
        username_box.send_keys("admin")
        password_box.send_keys("admin")
        login_button.click()

        
        time.sleep(3)
        self.assertIn("admin", self.driver.current_url)

        
        self.driver.save_screenshot("login_acceso.png")

    def test_login_invalid_credentials(self):
        """Prueba de inicio de sesión con credenciales incorrectas."""
        self.driver.get("http://localhost/biblioteca/")

        
        username_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "usuario"))
        )
        password_box = self.driver.find_element(By.ID, "clave")
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-block")

        
        username_box.send_keys("admind")
        password_box.send_keys("contraseña_invalida")
        login_button.click()

        
        error_alert = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "alerta"))
        )
        self.assertFalse("d-none" in error_alert.get_attribute("class"))

        
        self.driver.save_screenshot("login_acceso_invalido.png")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="./report",
            report_name="LoginTestReport",
            combine_reports=True
        ),
        verbosity=2
    )
