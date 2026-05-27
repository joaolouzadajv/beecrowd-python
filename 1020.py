# Lê o valor inteiro de entrada
total_dias = int(input())

# Calcula os anos
anos = total_dias // 365
resto = total_dias % 365

# Calcula os meses e dias restantes
meses = resto // 30
dias = resto % 30

# Exibe o resultado no formato solicitado
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")