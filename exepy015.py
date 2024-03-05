# Declaração das informações dos aparelhos
aparelhos = {
    "geladeira": {"potencia": 150, "horas_por_dia": 8},
    "freezer": {"potencia": 120, "horas_por_dia": 6},
    "chuveiro_eletrico": {"potencia": 4000, "horas_por_dia": 1},
    "lampada": {"potencia": 60, "horas_por_dia": 4}
}

# Definindo a quantidade de dias no mês
dias_por_mes = 30

# Solicitar o nome do produto ao usuário
nome_produto = input("Digite o nome do produto (geladeira, freezer, chuveiro_eletrico, lampada): ").lower()

# Verificar se o produto fornecido está na lista de aparelhos
if nome_produto in aparelhos:
    # Obter as informações do produto escolhido
    produto = aparelhos[nome_produto]

    # Calcular o consumo em kWh para o aparelho escolhido
    consumo_produto = (produto["potencia"] * produto["horas_por_dia"] * dias_por_mes) / 1000

    # Calcular o valor a ser pago pelo consumo do aparelho
    custo_por_kwh = 0.30  # em reais
    valor_total = consumo_produto * custo_por_kwh

    # Exibir os resultados
    print(f"Consumo do {nome_produto.capitalize()}: {consumo_produto:.2f} kWh")
    print(f"Valor total a ser pago: R$ {valor_total:.2f}")
else:
    print("Produto não encontrado. Certifique-se de digitar um nome válido.")