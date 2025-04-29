import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

class TestDemoBlaze(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = "https://www.demoblaze.com/"
        self.report = {
            "test_case": "TC-004",
            "objetivo": "Simular compra de um produto no DemoBlaze",
            "passos_executados": [],
            "dados_entrada": {},
            "resultados": [],
            "status": "Passou"
        }
        self.start_time = datetime.now()

    def test_purchase_flow(self):
        """TC-004: Simular compra de um produto"""
        try:
            driver = self.driver
            driver.get(self.base_url)
            
            # Registrar passo
            self.report["passos_executados"].append("1. Acessar página inicial")
            
            # Selecionar primeiro produto da lista (Samsung galaxy s6)
            product_link = driver.find_element(By.LINK_TEXT, "Samsung galaxy s6")
            product_link.click()
            
            # Registrar passo
            self.report["passos_executados"].append("2. Selecionar produto 'Samsung galaxy s6'")
            
            # Aguardar carregamento da página do produto
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "name"))
            )
            
            # Clicar em Add to cart
            add_to_cart = driver.find_element(By.LINK_TEXT, "Add to cart")
            add_to_cart.click()
            
            # Registrar passo
            self.report["passos_executados"].append("3. Adicionar produto ao carrinho")
            
            # Aguardar alerta e aceitar
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            
            # Verificar mensagem do alerta
            expected_alert = "Product added"
            self.assertIn(expected_alert, alert_text)
            self.report["resultados"].append(("TC-004 - Alerta", expected_alert, alert_text))
            
            # Ir para o carrinho
            cart_link = driver.find_element(By.ID, "cartur")
            cart_link.click()
            
            # Registrar passo
            self.report["passos_executados"].append("4. Acessar carrinho de compras")
            
            # Aguardar carregamento do carrinho
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Place Order')]"))
            )
            
            # Clicar em Place Order
            place_order = driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]")
            place_order.click()
            
            # Registrar passo
            self.report["passos_executados"].append("5. Iniciar processo de compra (Place Order)")
            
            # Preencher formulário de compra
            form_data = {
                "name": "Teste Silva",
                "country": "Brasil",
                "city": "São Paulo",
                "card": "1234567812345678",
                "month": "12",
                "year": "2025"
            }
            self.report["dados_entrada"] = form_data
            
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "name"))
            )
            
            for field, value in form_data.items():
                driver.find_element(By.ID, field).send_keys(value)
            
            # Registrar passo
            self.report["passos_executados"].append("6. Preencher formulário de compra")
            
            # Finalizar compra
            purchase_button = driver.find_element(By.XPATH, "//button[contains(text(),'Purchase')]")
            purchase_button.click()
            
            # Registrar passo
            self.report["passos_executados"].append("7. Finalizar compra (Purchase)")
            
            # Capturar dados da compra
            confirmation = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "sweet-alert"))
            )
            
            confirmation_text = confirmation.text
            self.report["resultados"].append(("TC-004 - Confirmação", "Modal de confirmação", confirmation_text))
            
            # Extrair ID do pedido e valor
            lines = confirmation_text.split("\n")
            order_id = None
            amount = None
            
            for line in lines:
                if "Id:" in line:
                    order_id = line.split("Id:")[1].strip()
                elif "Amount:" in line:
                    amount = line.split("Amount:")[1].strip()
            
            self.report["resultados"].append(("TC-004 - ID Pedido", "ID gerado", order_id))
            self.report["resultados"].append(("TC-004 - Valor", "Valor da compra", amount))
            
            # Fechar modal
            driver.find_element(By.XPATH, "//button[contains(text(),'OK')]").click()
            
        except Exception as e:
            self.report["status"] = "Falhou"
            self.report["resultados"].append(("TC-004", "Erro inesperado", str(e)))
            raise

    def tearDown(self):
        self.end_time = datetime.now()
        self.driver.quit()
        
        # Gerar relatório
        self.report["tempo_execucao"] = str(self.end_time - self.start_time)
        self.generate_report()

    def generate_report(self):
        """Gera relatório em formato Markdown"""
        report_path = "../relatorios/relatorio_demoblaze.md"
        with open(report_path, "w") as f:
            f.write(f"# Relatório de Testes - DemoBlaze\n\n")
            f.write(f"## Caso de Teste: {self.report['test_case']}\n\n")
            f.write(f"### Objetivo\n{self.report['objetivo']}\n\n")
            
            f.write("### Passos Executados\n")
            for i, passo in enumerate(self.report["passos_executados"], 1):
                f.write(f"{i}. {passo}\n")
            
            f.write("\n### Dados de Entrada\n")
            for campo, valor in self.report["dados_entrada"].items():
                f.write(f"- {campo}: {valor}\n")
            
            f.write("\n### Resultados\n")
            f.write("| Item | Esperado | Obtido |\n")
            f.write("|------|----------|--------|\n")
            for item, esperado, obtido in self.report["resultados"]:
                f.write(f"| {item} | {esperado} | {obtido} |\n")
            
            f.write(f"\n### Status: {self.report['status']}\n")
            f.write(f"\n### Tempo de Execução: {self.report['tempo_execucao']}\n")

if __name__ == "__main__":
    unittest.main()