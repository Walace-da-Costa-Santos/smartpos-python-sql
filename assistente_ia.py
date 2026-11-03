from google import genai
from google.genai import errors

from relatorios import obter_resumo_vendas, obter_pagamento_mais_usado


def gerar_dados_para_analise():
    resumo = obter_resumo_vendas()
    pagamento = obter_pagamento_mais_usado()

    return {
        "quantidade_vendas": resumo["quantidade_vendas"],
        "faturamento_total": resumo["faturamento_total"],
        "ticket_medio": resumo["ticket_medio"],
        "pagamento_mais_usado": pagamento["pagamento"],
        "quantidade_pagamento": pagamento["quantidade"]
    }


def gerar_analise_ia():
    dados = gerar_dados_para_analise()

    client = genai.Client()

    prompt = f"""
    Você é um assistente de análise de vendas.

    Analise os dados abaixo e escreva um resumo curto e simples
    para o comerciante.

    Use somente os dados fornecidos.
    Não invente informações.

    Quantidade de vendas: {dados["quantidade_vendas"]}
    Faturamento total: R$ {dados["faturamento_total"]:.2f}
    Ticket médio: R$ {dados["ticket_medio"]:.2f}
    Pagamento mais utilizado: {dados["pagamento_mais_usado"]}
    Quantidade de utilizações: {dados["quantidade_pagamento"]}
    """

    try:
        resposta = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return resposta.text

    except errors.ServerError:
        return "O assistente de IA está temporariamente indisponível. Tente novamente mais tarde."


