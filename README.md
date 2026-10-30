# 💳 SmartPOS — Sistema de Vendas com Python e SQL

O SmartPOS é um projeto desenvolvido em Python para simular o funcionamento básico de uma maquininha de cartão e praticar conceitos de programação, banco de dados e análise de dados.

O sistema permite registrar vendas, armazenar informações em um banco SQLite, consultar o histórico e gerar relatórios utilizando SQL.

## 🚀 Funcionalidades

- Pagamento no débito
- Crédito à vista
- Crédito parcelado de 2 a 12 vezes
- Validação dos valores informados
- Registro de data e hora das vendas
- Armazenamento das vendas em SQLite
- Consulta do histórico de vendas
- Relatório geral
- Relatório por forma de pagamento
- Relatório diário
- Relatório por data
- Cálculo do faturamento
- Cálculo do ticket médio
- Identificação da maior e menor venda
- Identificação da forma de pagamento mais utilizada
- Assistente interativo baseado em regras e palavras-chave

## 🛠️ Tecnologias

- Python
- SQL
- SQLite

## 📁 Estrutura do projeto

```text
SmartPOS/
│
├── main.py
├── database.py
├── pagamentos.py
├── relatorios.py
├── assistente.py
├── .gitignore
└── README.md