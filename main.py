from database import criar_tabela

from pagamentos import processar_pagamento

from relatorios import (
    consultar_vendas_banco,
    relatorio_vendas,
    relatorio_por_pagamento,
    relatorio_diario,
    relatorio_por_data,
    analise_vendas
)

from assistente import assistente_inteligente


def iniciar_maquininha():

    while True:

        print("\n========== SMARTPOS ==========")
        print("1 - Débito")
        print("2 - Crédito à vista")
        print("3 - Crédito parcelado")
        print("4 - Consultar vendas")
        print("5 - Relatório geral")
        print("6 - Relatório por pagamento")
        print("7 - Relatório de hoje")
        print("8 - Relatório por data")
        print("9 - Análise de vendas")
        print("10 - Assistente interativo")
        print("0 - Sair")
        print("==============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Obrigado por utilizar o SmartPOS!")
            break

        elif opcao in ["1", "2", "3"]:
            processar_pagamento(opcao)

        elif opcao == "4":
            consultar_vendas_banco()

        elif opcao == "5":
            relatorio_vendas()

        elif opcao == "6":
            relatorio_por_pagamento()

        elif opcao == "7":
            relatorio_diario()

        elif opcao == "8":
            relatorio_por_data()

        elif opcao == "9":
            analise_vendas()

        elif opcao == "10":
            assistente_inteligente()

        else:
            print("Opção inválida! Tente novamente.")


criar_tabela()
iniciar_maquininha()