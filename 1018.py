# Lê o valor inteiro N
valor = int(input())

# Imprime o valor lido
print(valor)

# Lista das notas disponíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Calcula a quantidade de cada nota
for nota in notas:
    quantidade_notas = valor // nota
    valor %= nota
    print(f"{quantidade_notas} nota(s) de R$ {nota},00")