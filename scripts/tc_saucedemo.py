import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

class TestSauceDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = "https://www.saucedemo.com/"
        self.report = {
            "test_case": "TC-001 e TC-002",
            "objetivo": "Testar login bem-sucedido e mal-sucedido no SauceDemo",
            "passos_executados": [],
            "dados_entrada": {},
            "resultados": [],
            "status": "Passou"
        }
        self.start_time = datetime.now()

    def test_login_sucesso(self):
        """TC-001: Login bem-sucedido com usuário padrão"""
        try:
            driver = self.driver
            driver.get(self.base_url)
            
            # Registrar passo
            step = "1. Acessar página de login"
            self.report["passos_executados"].append(step)
            
            # Dados de login válido
            username = "standard_user"
            password = "secret_sauce"
            self.report["dados_entrada"]["TC-001"] = {"username": username, "password": password}
            
            # Preencher formulário
            driver.find_element(By.ID, "user-name").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "login-button").click()
            
            # Registrar passo
            step = "2. Preencher credenciais e submeter"
            self.report["passos_executados"].append(step)
            
            # Verificar se login foi bem-sucedido
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
            )
            resultado = "Página de produtos carregada com sucesso"
            self.report["resultados"].append(("TC-001", "Página de produtos exibida", resultado))
            
        except Exception as e:
            self.report["status"] = "Falhou"
            self.report["resultados"].append(("TC-001", "Erro inesperado", str(e)))
            raise

    def test_login_falha(self):
        """TC-002: Login mal-sucedido com usuário inválido"""
        try:
            driver = self.driver
            driver.get(self.base_url)
            
            # Dados de login inválido
            username = "invalid_user"
            password = "wrong_password"
            self.report["dados_entrada"]["TC-002"] = {"username": username, "password": password}
            
            # Preencher formulário
            driver.find_element(By.ID, "user-name").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "login-button").click()
            
            # Verificar mensagem de erro
            error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))
            ).text
            expected_message = "Epic sadface: Username and password do not match any user in this service"
            
            self.assertIn(expected_message, error_message)
            self.report["resultados"].append(("TC-002", expected_message, error_message))
            
        except Exception as e:
            self.report["status"] = "Falhou"
            self.report["resultados"].append(("TC-002", "Erro inesperado", str(e)))
            raise

    def tearDown(self):
        self.end_time = datetime.now()
        self.driver.quit()
        
        # Gerar relatório
        self.report["tempo_execucao"] = str(self.end_time - self.start_time)
        self.generate_report()

    def generate_report(self):
        """Gera relatório em formato Markdown"""
        report_path = "../relatorios/relatorio_saucedemo.md"
        with open(report_path, "w") as f:
            f.write(f"# Relatório de Testes - SauceDemo\n\n")
            f.write(f"## Caso de Teste: {self.report['test_case']}\n\n")
            f.write(f"### Objetivo\n{self.report['objetivo']}\n\n")
            
            f.write("### Passos Executados\n")
            for i, passo in enumerate(self.report["passos_executados"], 1):
                f.write(f"{i}. {passo}\n")
            
            f.write("\n### Dados de Entrada\n")
            for tc, dados in self.report["dados_entrada"].items():
                f.write(f"- {tc}: {dados}\n")
            
            f.write("\n### Resultados\n")
            f.write("| TC | Esperado | Obtido |\n")
            f.write("|----|----------|--------|\n")
            for tc, esperado, obtido in self.report["resultados"]:
                f.write(f"| {tc} | {esperado} | {obtido} |\n")
            
            f.write(f"\n### Status: {self.report['status']}\n")
            f.write(f"\n### Tempo de Execução: {self.report['tempo_execucao']}\n")

if __name__ == "__main__":
    unittest.main()