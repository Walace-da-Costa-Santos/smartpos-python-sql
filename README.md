# 💳 SmartPOS — Python + SQL

Projeto desenvolvido em **Python e SQLite** para simular uma maquininha de cartão e aplicar conceitos de programação, banco de dados e análise de vendas.

## 🚀 Funcionalidades

- Pagamentos simulados no débito, crédito à vista e parcelado
- Registro das vendas em banco SQLite
- Histórico de vendas
- Relatórios por data e forma de pagamento
- Faturamento total e ticket médio
- Maior e menor venda
- Forma de pagamento mais utilizada
- Assistente interativo baseado em palavras-chave

## 🛠️ Tecnologias

- Python
- SQL
- SQLite
- Git e GitHub

## 📁 Estrutura

```text id="nqf8tc"
smartpos-python-sql/
├── main.py
├── database.py
├── pagamentos.py
├── relatorios.py
└── assistente.py
```

O projeto foi dividido em módulos para separar as responsabilidades de banco de dados, pagamentos, relatórios e assistente.

## ▶️ Executar

Clone o repositório:

```bash id="2n81jf"
git clone https://github.com/Walace-da-Costa-Santos/smartpos-python-sql.git
```

Entre na pasta:

```bash id="6z9ctw"
cd smartpos-python-sql
```

Execute:

```bash id="isxqf2"
python main.py
```

O banco SQLite é criado automaticamente.

## 📚 Conceitos praticados

Funções, condicionais, loops, tratamento de exceções, modularização, persistência de dados e consultas SQL com `SELECT`, `WHERE`, `GROUP BY`, `ORDER BY`, `COUNT`, `SUM`, `AVG`, `MAX` e `MIN`.

> Projeto educacional. Os pagamentos são apenas simulações e nenhum dado real de cartão é processado.
