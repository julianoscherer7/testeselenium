# Relatório de Testes - DemoBlaze

## Caso de Teste: TC-004

### Objetivo
Simular uma compra no site [DemoBlaze](https://www.demoblaze.com/), desde a seleção do produto até a confirmação do pedido.

---

### Passos Executados
1. Acessar a página inicial.
2. Selecionar o produto *"Samsung Galaxy S6"*.
3. Clicar em *"Add to cart"* e aceitar o alerta.
4. Acessar o carrinho.
5. Clicar em *"Place Order"*.
6. Preencher o formulário de compra:
   - Nome: `Teste Silva`
   - País: `Brasil`
   - Cidade: `São Paulo`
   - Cartão de crédito: `1234567812345678`
   - Mês: `12`
   - Ano: `2025`
7. Clicar em *"Purchase"*.
8. Validar a mensagem de confirmação.

---

### Dados de Entrada
```json
{
  "Nome": "Teste Silva",
  "País": "Brasil",
  "Cidade": "São Paulo",
  "Cartão": "1234567812345678",
  "Mês": "12",
  "Ano": "2025"
}