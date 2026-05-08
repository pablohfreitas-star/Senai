import math

# Dados do problema
metros_por_blusa = 120
metros_por_novelo = 125

# Entrada
qtd_blusas = int(input("Quantas blusas serão produzidas? "))

# Cálculo
total_metros_necessarios = qtd_blusas * metros_por_blusa

# Arredonda para cima
total_novelos = math.ceil(total_metros_necessarios / metros_por_novelo)

# Saída
print(f"Para produzir {qtd_blusas} blusas, você precisará comprar {total_novelos} novelos.")