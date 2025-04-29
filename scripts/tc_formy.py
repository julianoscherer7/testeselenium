import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

class TestFormy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = "https://formy-project.herokuapp.com/form"
        self.report = {
            "test_case": "TC-005",
            "objetivo": "Preencher e submeter formulário completo",
            "passos_executados": [],
            "dados_entrada": {},
            "valores_selecionados": {},
            "resultados": [],
            "status": "Passou"
        }
        self.start_time = datetime.now()

    def test_form_submission(self):
        """TC-005: Preencher e submeter formulário completo"""
        try:
            driver = self.driver
            driver.get(self.base_url)
            
            # Registrar passo
            self.report["passos_executados"].append("1. Acessar página do formulário")
            
            # Dados do formulário
            form_data = {
                "first_name": "João",
                "last_name": "Silva",
                "job_title": "QA Engineer",
                "address": "Rua Teste, 123",
                "email": "joao.silva@teste.com",
                "phone": "11999998888"
            }
            self.report["dados_entrada"] = form_data
            
            # Preencher campos básicos
            driver.find_element(By.ID, "first-name").send_keys(form_data["first_name"])
            driver.find_element(By.ID, "last-name").send_keys(form_data["last_name"])
            driver.find_element(By.ID, "job-title").send_keys(form_data["job_title"])
            driver.find_element(By.ID, "address").send_keys(form_data["address"])
            driver.find_element(By.ID, "email").send_keys(form_data["email"])
            driver.find_element(By.ID, "phone-number").send_keys(form_data["phone"])
            
            # Registrar passo
            self.report["passos_executados"].append("2. Preencher campos básicos do formulário")
            
            # Selecionar gênero (radio button)
            gender = "radio-button-2"  # Masculino
            driver.find_element(By.ID, gender).click()
            self.report["valores_selecionados"]["Gênero"] = "Masculino"
            
            # Selecionar experiência (checkbox)
            experience = "checkbox-1"  # 1-4 anos
            driver.find_element(By.ID, experience).click()
            self.report["valores_selecionados"]["Experiência"] = "1-4 anos"
            
            # Selecionar profissão (dropdown)
            education = Select(driver.find_element(By.ID, "select-menu"))
            education.select_by_value("3")  # College
            self.report["valores_selecionados"]["Educação"] = "College"
            
            # Selecionar ferramentas (multi-select)
            tools = driver.find_element(By.ID, "select-tool")
            tools.click()
            driver.find_element(By.XPATH, "//option[contains(text(),'Selenium')]").click()
            self.report["valores_selecionados"]["Ferramentas"] = "Selenium"
            
            # Selecionar continente (dropdown)
            continent = Select(driver.find_element(By.ID, "select-continent"))
            continent.select_by_visible_text("South America")
            self.report["valores_selecionados"]["Continente"] = "South America"
            
            # Selecionar comandos (multi-select)
            commands = Select(driver.find_element(By.ID, "select-selenium-commands"))
            commands.select_by_visible_text("Switch Commands")
            commands.select_by_visible_text("Wait Commands")
            selected_commands = [option.text for option in commands.all_selected_options]
            self.report["valores_selecionados"]["Comandos"] = ", ".join(selected_commands)
            
            # Registrar passo
            self.report["passos_executados"].append("3. Selecionar opções em campos complexos")
            
            # Submeter formulário
            submit_button = driver.find_element(By.XPATH, "//a[contains(text(),'Submit')]")
            submit_button.click()
            
            # Registrar passo
            self.report["passos_executados"].append("4. Submeter formulário")
            
            # Verificar mensagem de sucesso
            success_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "alert"))
            ).text
            
            expected_message = "The form was successfully submitted!"
            self.assertIn(expected_message, success_message)
            self.report["resultados"].append(("TC-005", expected_message, success_message))
            
        except Exception as e:
            self.report["status"] = "Falhou"
            self.report["resultados"].append(("TC-005", "Erro inesperado", str(e)))
            raise

    def tearDown(self):
        self.end_time = datetime.now()
        self.driver.quit()
        
        # Gerar relatório
        self.report["tempo_execucao"] = str(self.end_time - self.start_time)
        self.generate_report()

    def generate_report(self):
        """Gera relatório em formato Markdown"""
        report_path = "../relatorios/relatorio_formy.md"
        with open(report_path, "w") as f:
            f.write(f"# Relatório de Testes - Formy\n\n")
            f.write(f"## Caso de Teste: {self.report['test_case']}\n\n")
            f.write(f"### Objetivo\n{self.report['objetivo']}\n\n")
            
            f.write("### Passos Executados\n")
            for i, passo in enumerate(self.report["passos_executados"], 1):
                f.write(f"{i}. {passo}\n")
            
            f.write("\n### Dados de Entrada\n")
            for campo, valor in self.report["dados_entrada"].items():
                f.write(f"- {campo.replace('_', ' ').title()}: {valor}\n")
            
            f.write("\n### Valores Selecionados\n")
            for campo, valor in self.report["valores_selecionados"].items():
                f.write(f"- {campo}: {valor}\n")
            
            f.write("\n### Resultados\n")
            f.write("| TC | Esperado | Obtido |\n")
            f.write("|----|----------|--------|\n")
            for tc, esperado, obtido in self.report["resultados"]:
                f.write(f"| {tc} | {esperado} | {obtido} |\n")
            
            f.write(f"\n### Status: {self.report['status']}\n")
            f.write(f"\n### Tempo de Execução: {self.report['tempo_execucao']}\n")

if __name__ == "__main__":
    unittest.main()