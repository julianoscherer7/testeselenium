# Relatório de Testes - SauceDemo

## Caso de Teste: TC-001 e TC-002

### Objetivo
Testar login bem-sucedido e mal-sucedido no site [SauceDemo](https://www.saucedemo.com/).

---

### Passos Executados
1. Acessar a página de login.
2. Preencher o campo "Username" com `standard_user`.
3. Preencher o campo "Password" com `secret_sauce`.
4. Clicar no botão "Login".
5. Verificar se a página de produtos foi carregada.
6. Repetir o processo com credenciais inválidas (`invalid_user` / `wrong_password`).
7. Verificar mensagem de erro.

---

### Dados de Entrada
| Cenário       | Username        | Password       |
|---------------|----------------|----------------|
| Login válido  | `standard_user` | `secret_sauce` |
| Login inválido| `invalid_user`  | `wrong_password` |

---

### Resultados
| Teste  | Esperado | Obtido | Status |
|--------|----------|--------|--------|
| TC-001 | Redirecionar para página de produtos | ✅ Página de produtos carregada com sucesso | **Passou** |
| TC-002 | Exibir mensagem de erro: *"Epic sadface: Username and password do not match any user in this service"* | ✅ Mensagem exibida corretamente | **Passou** |

---

### Análise
- **TC-001**: O login com usuário padrão funcionou conforme esperado.
- **TC-002**: O sistema exibiu a mensagem de erro correta para credenciais inválidas.

⏳ **Tempo de execução**: 12 segundos