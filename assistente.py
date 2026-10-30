from database import conectar_banco


def obter_resumo_vendas():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            SUM(valor),
            AVG(valor),
            MAX(valor),
            MIN(valor)
        FROM vendas
    """)

    resultado = cursor.fetchone()

    quantidade = resultado[0]
    faturamento = resultado[1] or 0
    media = resultado[2] or 0
    maior_venda = resultado[3] or 0
    menor_venda = resultado[4] or 0

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

    if pagamento:
        pagamento_mais_utilizado = pagamento[0]
    else:
        pagamento_mais_utilizado = "Nenhum"

    resumo = {
        "quantidade_vendas": quantidade,
        "faturamento": faturamento,
        "ticket_medio": media,
        "maior_venda": maior_venda,
        "menor_venda": menor_venda,
        "pagamento_mais_utilizado": pagamento_mais_utilizado
    }

    return resumo


def contem_palavra(pergunta, palavras):
    for palavra in palavras:
        if palavra in pergunta:
            return True

    return False


def assistente_inteligente():
    resumo = obter_resumo_vendas()

    if resumo["quantidade_vendas"] == 0:
        print("\nAinda não existem vendas para analisar.")
        return

    print("\n========== ASSISTENTE SMARTPOS ==========")
    print("Faça perguntas sobre suas vendas.")
    print("Digite 'sair' para voltar ao menu.")
    print("=========================================")

    while True:
        pergunta = input("\nVocê: ").lower().strip()

        if pergunta == "sair":
            print("Saindo do assistente...")
            break

        elif contem_palavra(
            pergunta,
            ["faturamento", "faturei", "vendi", "total vendido"]
        ):
            print(
                "\nSmartPOS: "
                f"Seu faturamento total é de "
                f"R$ {resumo['faturamento']:.2f}."
            )

        elif contem_palavra(
            pergunta,
            ["ticket", "média", "media"]
        ):
            print(
                "\nSmartPOS: "
                f"Seu ticket médio é de "
                f"R$ {resumo['ticket_medio']:.2f}."
            )

        elif contem_palavra(
            pergunta,
            ["maior venda", "venda mais alta", "maior valor"]
        ):
            print(
                "\nSmartPOS: "
                f"Sua maior venda foi de "
                f"R$ {resumo['maior_venda']:.2f}."
            )

        elif contem_palavra(
            pergunta,
            ["menor venda", "venda mais baixa", "menor valor"]
        ):
            print(
                "\nSmartPOS: "
                f"Sua menor venda foi de "
                f"R$ {resumo['menor_venda']:.2f}."
            )

        elif contem_palavra(
            pergunta,
            ["pagamento", "forma de pagamento"]
        ):
            print(
                "\nSmartPOS: "
                "A forma de pagamento mais utilizada foi "
                f"{resumo['pagamento_mais_utilizado']}."
            )

        elif contem_palavra(
            pergunta,
            ["quantas vendas", "quantidade de vendas"]
        ):
            print(
                "\nSmartPOS: "
                f"Foram realizadas "
                f"{resumo['quantidade_vendas']} vendas."
            )

        else:
            print(
                "\nSmartPOS: "
                "Não consegui entender sua pergunta."
            )