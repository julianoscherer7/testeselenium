# Relatório de Testes - Dynamic Loading

## Caso de Teste: TC-003

### Objetivo
Verificar se o texto *"Hello World!"* aparece após clicar no botão *"Start"* no site [Dynamic Loading](https://the-internet.herokuapp.com/dynamic_loading).

---

### Passos Executados
1. Acessar a página *"Dynamic Loading"*.
2. Clicar em *"Example 1"*.
3. Clicar no botão *"Start"*.
4. Aguardar até que o texto *"Hello World!"* seja exibido.
5. Verificar se o texto aparece dentro do tempo limite (10 segundos).

---

### Resultados
| Teste  | Esperado | Obtido | Status |
|--------|----------|--------|--------|
| TC-003 | Texto *"Hello World!"* deve aparecer após carregamento | ✅ Texto exibido após **5 segundos** | **Passou** |

---

### Análise
- O sistema aguardou corretamente o carregamento dinâmico.
- O tempo de espera foi de **5 segundos**, dentro do limite estabelecido.

⏳ **Tempo de execução**: 8 segundos