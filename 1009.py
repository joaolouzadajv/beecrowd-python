# Leitura dos dados de entrada
nome = input()
salario_fixo = float(input())
vendas_total = float(input())

# Cálculo da comissão (15%) e do salário final
comissao = vendas_total * 0.15
total_receber = salario_fixo + comissao

# Impressão do resultado com duas casas decimais
# O formato "TOTAL = R$ {:.2f}" garante os espaços e a pontuação correta
print(f"TOTAL = R$ {total_receber:.2f}")