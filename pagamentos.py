from datetime import datetime

from database import salvar_venda


def obter_valor():
    while True:
        try:
            valor = float(
                input("Digite o valor da venda: R$ ").replace(",", ".")
            )

            if valor > 0:
                return valor

            print("O valor precisa ser maior que zero.")

        except ValueError:
            print("Digite um valor válido.")


def obter_parcelas():
    while True:
        try:
            parcelas = int(
                input("Em quantas vezes? (2 a 12): ")
            )

            if 2 <= parcelas <= 12:
                return parcelas

            print("Escolha entre 2 e 12 parcelas.")

        except ValueError:
            print("Digite um número inteiro válido.")


def processar_pagamento(opcao):

    valor = obter_valor()

    if opcao == "1":
        forma_pagamento = "Débito"
        parcelas = 1

    elif opcao == "2":
        forma_pagamento = "Crédito à vista"
        parcelas = 1

    elif opcao == "3":
        forma_pagamento = "Crédito parcelado"
        parcelas = obter_parcelas()

    else:
        print("Forma de pagamento inválida.")
        return

    valor_parcela = valor / parcelas

    data_venda = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )

    venda = {
        "valor": valor,
        "pagamento": forma_pagamento,
        "parcelas": parcelas,
        "valor_parcela": valor_parcela,
        "data_venda": data_venda
    }

    salvar_venda(venda)

    print("\n========== COMPROVANTE ==========")
    print(f"Data da venda: {data_venda}")
    print(f"Valor da venda: R$ {valor:.2f}")
    print(f"Pagamento: {forma_pagamento}")
    print(f"Parcelas: {parcelas}x")
    print(f"Valor por parcela: R$ {valor_parcela:.2f}")
    print("Status: APROVADO ")
    print("================================")