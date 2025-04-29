
---

## **Relatório - Formy** (`relatorio_formy.md`)

```markdown
# Relatório de Testes - Formy

## Caso de Teste: TC-005

### Objetivo
Preencher e submeter o formulário completo no site [Formy](https://formy-project.herokuapp.com/form).

---

### Passos Executados
1. Acessar a página do formulário.
2. Preencher campos obrigatórios:
   - Nome: `João`
   - Sobrenome: `Silva`
   - Profissão: `QA Engineer`
   - E-mail: `joao.silva@teste.com`
   - Telefone: `11999998888`
3. Selecionar opções:
   - Gênero: *Masculino* (Radio Button)
   - Experiência: *1-4 anos* (Checkbox)
   - Educação: *College* (Dropdown)
   - Ferramentas: *Selenium* (Multi-select)
   - Continente: *South America* (Dropdown)
   - Comandos: *Switch Commands, Wait Commands* (Multi-select)
4. Clicar em *"Submit"*.
5. Verificar mensagem de sucesso.

---

### Dados de Entrada
```json
{
  "Nome": "João",
  "Sobrenome": "Silva",
  "Profissão": "QA Engineer",
  "E-mail": "joao.silva@teste.com",
  "Telefone": "11999998888",
  "Gênero": "Masculino",
  "Experiência": "1-4 anos",
  "Educação": "College",
  "Ferramentas": "Selenium",
  "Continente": "South America",
  "Comandos": ["Switch Commands", "Wait Commands"]
}