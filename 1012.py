# Leitura dos três valores de ponto flutuante
entrada = input().split()
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

# Cálculos das áreas
triangulo = (A * C) / 2
circulo = 3.14159 * (C ** 2)
trapezio = ((A + B) * C) / 2
quadrado = B * B
retangulo = A * B

# Exibição dos resultados com 3 casas decimais
print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")