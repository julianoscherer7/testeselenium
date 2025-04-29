import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

class TestDynamicLoading(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = "https://the-internet.herokuapp.com/dynamic_loading"
        self.report = {
            "test_case": "TC-003",
            "objetivo": "Validar carregamento dinâmico do texto 'Hello World!'",
            "passos_executados": [],
            "resultados": [],
            "status": "Passou",
            "tempo_espera": None
        }
        self.start_time = datetime.now()

    def test_dynamic_loading(self):
        """TC-003: Aguardar carregamento do texto 'Hello World!'"""
        try:
            driver = self.driver
            driver.get(self.base_url)
            
            # Clicar no primeiro exemplo (Example 1)
            driver.find_element(By.PARTIAL_LINK_TEXT, "Example 1").click()
            
            # Registrar passo
            self.report["passos_executados"].append("1. Acessar página de dynamic loading")
            self.report["passos_executados"].append("2. Clicar em 'Example 1'")
            
            # Clicar no botão Start
            start_button = driver.find_element(By.XPATH, "//button[contains(text(),'Start')]")
            start_button.click()
            
            # Registrar passo
            self.report["passos_executados"].append("3. Clicar no botão Start")
            
            # Medir tempo de espera
            start_wait = time.time()
            
            # Aguardar texto aparecer (com timeout de 10 segundos)
            hello_text = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4[contains(text(),'Hello World!')]"))
            )
            
            end_wait = time.time()
            wait_time = end_wait - start_wait
            self.report["tempo_espera"] = f"{wait_time:.2f} segundos"
            
            # Verificar se texto está visível
            self.assertTrue(hello_text.is_displayed())
            self.report["resultados"].append(("TC-003", "Texto 'Hello World!' visível", "Texto encontrado e visível"))
            
        except Exception as e:
            self.report["status"] = "Falhou"
            self.report["resultados"].append(("TC-003", "Erro inesperado", str(e)))
            raise

    def tearDown(self):
        self.end_time = datetime.now()
        self.driver.quit()
        
        # Gerar relatório
        self.report["tempo_execucao"] = str(self.end_time - self.start_time)
        self.generate_report()

    def generate_report(self):
        """Gera relatório em formato Markdown"""
        report_path = "../relatorios/relatorio_dynamic_loading.md"
        with open(report_path, "w") as f:
            f.write(f"# Relatório de Testes - Dynamic Loading\n\n")
            f.write(f"## Caso de Teste: {self.report['test_case']}\n\n")
            f.write(f"### Objetivo\n{self.report['objetivo']}\n\n")
            
            f.write("### Passos Executados\n")
            for i, passo in enumerate(self.report["passos_executados"], 1):
                f.write(f"{i}. {passo}\n")
            
            f.write(f"\n### Tempo de Espera: {self.report['tempo_espera']}\n")
            
            f.write("\n### Resultados\n")
            f.write("| TC | Esperado | Obtido |\n")
            f.write("|----|----------|--------|\n")
            for tc, esperado, obtido in self.report["resultados"]:
                f.write(f"| {tc} | {esperado} | {obtido} |\n")
            
            f.write(f"\n### Status: {self.report['status']}\n")
            f.write(f"\n### Tempo de Execução: {self.report['tempo_execucao']}\n")

if __name__ == "__main__":
    unittest.main()