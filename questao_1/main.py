def calcular_valor_total(compras):
    total = 0
    for produto, categoria, valor in compras:
        total += valor
    return total


def calcular_valor_frutas_verduras(compras):
    total_fv = 0
    for produto, categoria, valor in compras:
        if categoria == "fruta" or categoria == "verdura":
            total_fv += valor
    return total_fv


def calcular_percentual_desconto(cliente_fidelidade, idade_cliente, valor_frutas_verduras):
    desconto = 0

    if idade_cliente > 60:
        desconto += 10

    if cliente_fidelidade:
        desconto += 5

    if valor_frutas_verduras > 30:
        desconto += 5

    if desconto > 20:
        desconto = 20

    return desconto


def exibir_resumo_compra(valor_total, valor_frutas_verduras, percentual_desconto):
    valor_final = valor_total * (1 - percentual_desconto / 100)

    print("===== RESUMO DA COMPRA =====")
    print(f"Valor original: R$ {valor_total:.2f}")
    print(f"Valor de frutas e verduras: R$ {valor_frutas_verduras:.2f}")
    print(f"Desconto aplicado: {percentual_desconto}%")
    print(f"Valor final: R$ {valor_final:.2f}")


compras = [
    ("Banana", "fruta", 8.50),
    ("Arroz", "mercado", 25.00),
    ("Tomate", "verdura", 12.00),
    ("Sabão", "limpeza", 18.00)
]

cliente_fidelidade = True
idade_cliente = 67

valor_total = calcular_valor_total(compras)
valor_fv = calcular_valor_frutas_verduras(compras)
percentual_desconto = calcular_percentual_desconto(cliente_fidelidade, idade_cliente, valor_fv)

exibir_resumo_compra(valor_total, valor_fv, percentual_desconto)