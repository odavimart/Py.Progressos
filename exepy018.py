# Inicialização das variáveis
total_respostas = 0
contagem_sistemas = [0] * 7  # Lista para armazenar a contagem de cada sistema

# Entrada de dados
while True:
    try:
        resposta = int(input("Informe o número correspondente ao melhor sistema (0 a 6, 0 para encerrar): "))

        # Verificar se a resposta está dentro do intervalo válido
        if 0 <= resposta <= 6:
            if resposta == 0:
                break  # Encerrar a entrada de dados quando for informado o valor 0
            else:
                contagem_sistemas[resposta] += 1
                total_respostas += 1
        else:
            print("Por favor, informe um valor entre 0 e 6.")
    except ValueError:
        print("Por favor, informe um valor numérico.")

# Calcular percentual de cada sistema
percentuais = [(contagem / total_respostas) * 100 if total_respostas > 0 else 0 for contagem in contagem_sistemas]

# Exibir resultados
print("\nResultados da Enquete:")
for i in range(1, 7):
    print(f"{i}- {percentuais[i]:.2f}% para {contagem_sistemas[i]} votos")

# Verificar se houve votos
if total_respostas > 0:
    print(f"\nTotal de {total_respostas} votos registrados.")
else:
    print("Nenhum voto registrado.")
