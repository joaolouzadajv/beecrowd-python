# Leitura dos dados do primeiro produto
linha1 = input().split()
codigo1 = int(linha1[0])
quantidade1 = int(linha1[1])
preco1 = float(linha1[2])

# Leitura dos dados do segundo produto
linha2 = input().split()
codigo2 = int(linha2[0])
quantidade2 = int(linha2[1])
preco2 = float(linha2[2])

# Cálculo do valor total
total = (quantidade1 * preco1) + (quantidade2 * preco2)

# Exibição do resultado formatado com 2 casas decimais
print(f"VALOR A PAGAR: R$ {total:.2f}")