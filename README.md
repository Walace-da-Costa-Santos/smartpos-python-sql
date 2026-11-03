# 💳 SmartPOS — Python + SQL + IA

Projeto desenvolvido em **Python e SQLite** para simular uma maquininha de cartão e aplicar conceitos de programação, banco de dados, análise de vendas e integração com IA.

## 🚀 Funcionalidades

- Pagamentos simulados no débito, crédito à vista e parcelado
- Registro das vendas em banco SQLite
- Histórico de vendas
- Relatórios por data e forma de pagamento
- Faturamento total e ticket médio
- Maior e menor venda
- Forma de pagamento mais utilizada
- **SmartPOS Insights:** análise das vendas em linguagem natural utilizando Gemini API

## 🤖 SmartPOS Insights

O SmartPOS Insights utiliza os dados calculados pelo **Python e SQL** e os envia para um modelo Gemini, responsável por transformar os resultados em uma explicação simples sobre as vendas.

Os cálculos são realizados pelo próprio sistema. A IA recebe os resultados das consultas para gerar o resumo, sem ser responsável pelo cálculo dos valores.

Fluxo da funcionalidade:

```text
SQLite
   ↓
SQL
   ↓
Python
   ↓
Dados das vendas
   ↓
Gemini API
   ↓
Análise em linguagem natural
```

## 🛠️ Tecnologias

- Python
- SQL
- SQLite
- Gemini API
- Git
- GitHub

## 📁 Estrutura

```text
smartpos-python-sql/
├── main.py
├── database.py
├── pagamentos.py
├── relatorios.py
├── assistente_ia.py
├── .gitignore
└── README.md
```

O projeto foi dividido em módulos para separar as responsabilidades de banco de dados, pagamentos, relatórios e análise com IA.

## ▶️ Executar

Clone o repositório:

```bash
git clone https://github.com/Walace-da-Costa-Santos/smartpos-python-sql.git
```

Entre na pasta:

```bash
cd smartpos-python-sql
```

Instale a biblioteca utilizada para integração com Gemini:

```bash
pip install -U google-genai
```

Configure a variável de ambiente `GEMINI_API_KEY` com sua própria chave da Gemini API.

Depois execute:

```bash
python main.py
```

O banco SQLite é criado automaticamente.

## 📚 Conceitos praticados

Funções, condicionais, loops, tratamento de exceções, modularização, persistência de dados, integração com API de IA e consultas SQL utilizando `SELECT`, `WHERE`, `GROUP BY`, `ORDER BY`, `COUNT`, `SUM`, `AVG`, `MAX` e `MIN`.

> Projeto educacional. Os pagamentos são apenas simulações e nenhum dado real de cartão ou cliente é processado. A chave da API não é armazenada no repositório.