import sqlite3


def conectar_banco():
    conexao = sqlite3.connect("smartpos.db")
    return conexao


def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            valor REAL NOT NULL,
            pagamento TEXT NOT NULL,
            parcelas INTEGER NOT NULL,
            valor_parcela REAL NOT NULL
        )
    """)

    cursor.execute("PRAGMA table_info(vendas)")
    colunas = cursor.fetchall()

    nomes_colunas = [coluna[1] for coluna in colunas]

    if "data_venda" not in nomes_colunas:
        cursor.execute("""
            ALTER TABLE vendas
            ADD COLUMN data_venda TEXT
        """)

    conexao.commit()
    conexao.close()


def salvar_venda(venda):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO vendas
        (
            valor,
            pagamento,
            parcelas,
            valor_parcela,
            data_venda
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        venda["valor"],
        venda["pagamento"],
        venda["parcelas"],
        venda["valor_parcela"],
        venda["data_venda"]
    ))

    conexao.commit()
    conexao.close()

    print("Venda salva no banco de dados!")