import math

# Lendo os três valores inteiros
entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

# Fórmula para encontrar o maior entre dois números
maior_ab = (a + b + abs(a - b)) // 2

# Comparando o resultado com o terceiro valor (c)
maior_final = (maior_ab + c + abs(maior_ab - c)) // 2

# Exibindo o resultado conforme solicitado
print(f"{maior_final} eh o maior")