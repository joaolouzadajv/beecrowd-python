# Leitura do raio
raio = float(input())

# Definição de pi
pi = 3.14159

# Cálculo do volume da esfera
# Usamos 4.0/3 para garantir a precisão de ponto flutuante
volume = (4.0 / 3) * pi * (raio ** 3)

# Exibição do resultado com 3 casas decimais
print(f"VOLUME = {volume:.3f}")