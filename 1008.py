# Leitura dos dados de entrada
numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Impressão dos resultados conforme a formatação exigida
print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = U$ {salario:.2f}")