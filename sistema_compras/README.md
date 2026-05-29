# Sistema de Compras Interativo 🛒

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen.svg)]()

Um sistema de simulação de fechamento de compras de supermercado executado diretamente no terminal. O projeto foi desenvolvido com foco especial na **Experiência do Usuário (UX)** e na **Robustez do Código**, garantindo que o programa guie o fluxo sem interrupções ou quebras por digitação incorreta.

---

## 🚀 Funcionalidades

- **Cadastro Dinâmico:** Adição de múltiplos produtos informando nome, preço unitário e quantidade.
- **Validação de Dados Estrita:** O sistema não aceita campos em branco, preços negativos ou quantidades menores/iguais a zero.
- **Tratamento de Exceções:** Implementação de blocos de controle que impedem o fechamento do programa caso o usuário digite letras em campos numéricos.
- **Menu de Pagamento Integrado:** Suporte para pagamentos via **PIX**, **Débito** e **Crédito**.
- **Cálculo de Parcelamento:** Divisão automatizada do valor total com exibição do valor de cada parcela no cartão de crédito.
- **Emissão de Nota Fiscal:** Geração de um cupom fiscal detalhado no fechamento, listando o subtotal de cada item e a forma de pagamento escolhida.

---

## 🛠️ Conceitos e Tecnologias Aplicadas

* **Estruturas de Repetição (`while True`):** Utilizadas para criar menus interativos e loops de validação contínua.
* **Tratamento de Erros (`try/except`):** Captura de erros do tipo `ValueError` para assegurar a integridade do fluxo de dados.
* **Estruturas de Dados Dinâmicas:** Uso de **Listas** para armazenar o carrinho e **Dicionários** para indexar as propriedades de cada produto.
* **Manipulação de Strings:** Aplicação de métodos como `.strip()` (remoção de espaços inúteis) e `.upper()` (padronização de respostas).
* **Formatação Monetária:** Uso de f-strings com formatação de casas decimais (`:.2f`).

---

## 💻 Como Executar o Projeto

1. Certifique-se de ter o Python instalado na sua máquina.
2. Navegue até a pasta do projeto pelo terminal:
   ```bash
   cd sistema_compras
