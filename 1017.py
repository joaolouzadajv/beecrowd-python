# Leitura dos valores de entrada
tempo = int(input())
velocidade = int(input())

# Cálculo da distância
distancia = tempo * velocidade

# Cálculo da quantidade de litros
litros = distancia / 12

# Exibição do resultado com três casas decimais
print(f"{litros:.3f}")