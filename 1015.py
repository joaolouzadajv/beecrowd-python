import math

# Leitura dos valores de entrada
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# Cálculo da distância
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Exibição do resultado com 4 casas decimais
print(f"{distancia:.4f}")