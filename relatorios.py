from datetime import datetime

from database import conectar_banco


def consultar_vendas_banco():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id,
            valor,
            pagamento,
            parcelas,
            valor_parcela,
            data_venda
        FROM vendas
        ORDER BY id
    """)

    vendas = cursor.fetchall()

    conexao.close()

    print("\n========== VENDAS NO BANCO ==========")

    if not vendas:
        print("Nenhuma venda cadastrada.")
        return

    for venda in vendas:
        print(f"ID: {venda[0]}")
        print(f"Valor: R$ {venda[1]:.2f}")
        print(f"Pagamento: {venda[2]}")
        print(f"Parcelas: {venda[3]}x")
        print(f"Valor da parcela: R$ {venda[4]:.2f}")

        if venda[5]:
            print(f"Data: {venda[5]}")
        else:
            print("Data: venda registrada antes da atualização")

        print("------------------------------------")


def relatorio_vendas():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            SUM(valor),
            AVG(valor)
        FROM vendas
    """)

    resultado = cursor.fetchone()

    conexao.close()

    quantidade = resultado[0]
    faturamento = resultado[1] or 0
    media = resultado[2] or 0

    print("\n========== RELATÓRIO GERAL ==========")
    print(f"Quantidade de vendas: {quantidade}")
    print(f"Faturamento total: R$ {faturamento:.2f}")
    print(f"Ticket médio: R$ {media:.2f}")
    print("====================================")


def relatorio_por_pagamento():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            pagamento,
            COUNT(*),
            SUM(valor)
        FROM vendas
        GROUP BY pagamento
        ORDER BY COUNT(*) DESC
    """)

    resultados = cursor.fetchall()

    conexao.close()

    print("\n======= VENDAS POR PAGAMENTO =======")

    if not resultados:
        print("Nenhuma venda cadastrada.")
        return

    for resultado in resultados:
        pagamento = resultado[0]
        quantidade = resultado[1]
        total = resultado[2]

        print(f"\nPagamento: {pagamento}")
        print(f"Quantidade: {quantidade}")
        print(f"Total vendido: R$ {total:.2f}")
        print("-----------------------------------")


def relatorio_diario():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    hoje = datetime.now().strftime("%d/%m/%Y")

    cursor.execute("""
        SELECT
            COUNT(*),
            SUM(valor),
            AVG(valor)
        FROM vendas
        WHERE data_venda LIKE ?
    """, (hoje + "%",))

    resultado = cursor.fetchone()

    conexao.close()

    quantidade = resultado[0]
    faturamento = resultado[1] or 0
    media = resultado[2] or 0

    print("\n========== RELATÓRIO DO DIA ==========")
    print(f"Data: {hoje}")
    print(f"Quantidade de vendas: {quantidade}")
    print(f"Faturamento: R$ {faturamento:.2f}")
    print(f"Ticket médio: R$ {media:.2f}")
    print("======================================")


def obter_data():
    while True:
        data = input("Digite a data (DD/MM/AAAA): ")

        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data

        except ValueError:
            print("Data inválida. Digite no formato DD/MM/AAAA.")


def relatorio_por_data():
    data = obter_data()

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            SUM(valor),
            AVG(valor)
        FROM vendas
        WHERE data_venda LIKE ?
    """, (data + "%",))

    resultado = cursor.fetchone()

    conexao.close()

    quantidade = resultado[0]
    faturamento = resultado[1] or 0
    media = resultado[2] or 0

    print(f"\n========== RELATÓRIO DE {data} ==========")

    if quantidade == 0:
        print("Nenhuma venda encontrada nessa data.")
        return

    print(f"Quantidade de vendas: {quantidade}")
    print(f"Faturamento: R$ {faturamento:.2f}")
    print(f"Ticket médio: R$ {media:.2f}")
    print("========================================")


def analise_vendas():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            MAX(valor),
            MIN(valor)
        FROM vendas
    """)

    valores = cursor.fetchone()

    maior_venda = valores[0]
    menor_venda = valores[1]

    cursor.execute("""
        SELECT
            pagamento,
            COUNT(*) AS quantidade
        FROM vendas
        GROUP BY pagamento
        ORDER BY quantidade DESC
        LIMIT 1
    """)

    pagamento = cursor.fetchone()

    conexao.close()

    print("\n========== ANÁLISE DE VENDAS ==========")

    if maior_venda is None:
        print("Nenhuma venda cadastrada.")
        return

    print(f"Maior venda: R$ {maior_venda:.2f}")
    print(f"Menor venda: R$ {menor_venda:.2f}")

    if pagamento:
        print(f"Pagamento mais utilizado: {pagamento[0]}")
        print(f"Quantidade de utilizações: {pagamento[1]}")

    print("=======================================")

def obter_resumo_vendas():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            SUM(valor),
            AVG(valor)
        FROM vendas
    """)

    resultado = cursor.fetchone()

    conexao.close()

    quantidade = resultado[0]
    faturamento = resultado[1] or 0
    ticket_medio = resultado[2] or 0

    return {
        "quantidade_vendas": quantidade,
        "faturamento_total": faturamento,
        "ticket_medio": ticket_medio
    }
def obter_pagamento_mais_usado():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            pagamento,
            COUNT(*) AS quantidade
        FROM vendas
        GROUP BY pagamento
        ORDER BY quantidade DESC
        LIMIT 1
    """)

    resultado = cursor.fetchone()

    conexao.close()

    if resultado is None:
        return {
            "pagamento": None,
            "quantidade": 0
        }

    return {
        "pagamento": resultado[0],
        "quantidade": resultado[1]
    }


