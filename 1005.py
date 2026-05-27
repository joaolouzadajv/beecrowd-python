# Leitura dos valores de ponto flutuante
A = float(input())
B = float(input())

# Cálculo da média ponderada
# Pesos: A = 3.5, B = 7.5. Soma dos pesos = 11.0
media = (A * 3.5 + B * 7.5) / 11.0

# Exibição do resultado com 5 casas decimais
print(f"MEDIA = {media:.5f}"    )