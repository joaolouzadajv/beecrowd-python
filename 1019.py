# Lê o valor inteiro N
n = int(input())

# Calcula as horas, minutos e segundos
horas = n // 3600
resto = n % 3600
minutos = resto // 60
segundos = resto % 60

# Exibe o resultado no formato horas:minutos:segundos
print(f"{horas}:{minutos}:{segundos}")